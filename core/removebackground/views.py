import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from rembg import remove
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from .forms import ImageUploadForm

def remove_background(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            
            fs = FileSystemStorage()
            # Save the uploaded file
            input_path = fs.save(image.name, image)
            input_full_path = fs.path(input_path)
            
            try:
                # Process the image using rembg
                with open(input_full_path, 'rb') as f:
                    input_image = f.read()
                
                output_image = remove(input_image)

                # Define output path and save processed image
                output_name = f"processed_{image.name}"
                output_path = os.path.join('media', output_name)
                with open(output_path, 'wb') as f:
                    f.write(output_image)
                
                context = {
                    'processed_image_url': f"/media/{output_name}",
                    'download_url': f"/media/{output_name}",
                }

                return render(request, 'remove/remove_background.html', context)
            except UnidentifiedImageError:
                context = {'error': "Invalid image file. Please upload a valid image."}
                return render(request, 'remove/remove_background.html', context)
            except Exception as e:
                context = {'error': f"An error occurred: {str(e)}"}
                return render(request, 'remove/remove_background.html', context)
            finally:
                # Cleanup: Remove the original uploaded file
                fs.delete(input_path)

    else:
        form = ImageUploadForm()

    return render(request, 'remove/remove_background.html', {'form': form})
