
from django.shortcuts import render,redirect
from .models import *
from PIL import Image
import os
from datetime import datetime
from django.conf import settings
import pickle
from django.contrib.auth.decorators import login_required

@login_required(login_url ="/loginp/")
def uploadImg(request):
    # return render(request,'formImgUpload.html')
    queryset=Medical.objects
    if request.method == 'POST':
        image = request.FILES['image']
        
        queryset.create(Eimage=image)
        # queryset.save()
        
        # Extract metadata
        image_path = os.path.join(settings.BASE_DIR, 'public', 'static', 'medical', str(image))
        model_path="C://Users/Rishabh Tiwari/Downloads/narlov/CodingForAll/core/public/static/model.pkl"
        with open(model_path,'rb')as f:
            model=pickle.load(f)

        img=cv2.imdecode(np.fromstring(image.read(),np.uint8),cv2.IMREAD_COLOR)
        img=cv2.resize(img,(180,180))
        prediction=model.predict(img.reshape(1,-1))
        print(prediction)
        # metadata = extract_metadata(image_path)
        image = Image.open(image_path)
        metadata = {
        'image_name': os.path.basename(image_path),
        'upload_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'image_size': os.path.getsize(image_path),
        'image_dimensions': image.size,
        # Add more metadata as needed
            }
        print(metadata)
        return render(request, 'formImgUpload.html', {'image_path': image_path, 'metadata': metadata})
    
    return render(request, 'formImgUpload.html')



# def upload_image(request):
#     queryset=Medical.objects
#     if request.method == 'POST':
#         image = request.FILES['image']
#         queryset.create(Eimage=image)
#         queryset.save()
        
#         # Extract metadata
#         metadata = extract_metadata(image_path)
        
#         return render(request, 'image_upload.html', {'image_path': image_path, 'metadata': metadata})
    
#     return render(request, 'image_upload.html')

# Create your views here.
