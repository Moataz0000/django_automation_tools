from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            valid_mime_types = ['image/jpeg', 'image/png', 'image/gif']
            if image.content_type not in valid_mime_types:
                raise forms.ValidationError("Unsupported file type. Please upload a JPEG, PNG, or GIF image.")
            if image.size > 5 * 1024 * 1024:  # 5 MB limit
                raise forms.ValidationError("Image file is too large ( > 5MB ).")
        return image
