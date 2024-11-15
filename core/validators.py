import os
from django.core.exceptions import ValidationError

def validate_file(file):
    ext = os.path.splitext(file.name)[1].lower()
    valid_image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    valid_video_extensions = ['.mp4', '.avi', '.mkv' , '.mov']

    image_max_size = 10 * 1024 * 1024  #10 MB
    video_max_size = 50 * 1024 * 1024  #50 MB

    if ext in valid_image_extensions:
        if file.size > image_max_size:
            raise ValidationError("Image size should not be more than 10 MB")
    elif ext in valid_video_extensions:
        if file.size > video_max_size:
            raise ValidationError("Videp size should not be more than 50 MB")
    else:
        raise ValidationError(
            "Invalid file type. Only image (jpg, jpeg, png) and video (mp4, mov, mkv) files can be uploaded.")
