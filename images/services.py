import cloudinary.uploader

def upload_to_cloudinary(file):
    try:
        result = cloudinary.uploader.upload(file)
        return {
            'url': result['secure_url'],
            'public_id': result['public_id']
        }
    except Exception as e:
        raise Exception(f"Не удалось выполнить загрузку из облачного хранилища: {str(e)}")
