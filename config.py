import os
from os.path import join, dirname, realpath

class Config (object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "6^0)1!0)5%1!4$1!1!9("

    abspath = dirname(realpath(__file__))
    UPLOAD_FOLDER = join(abspath, "app/client/upload")
    DOWNLOAD_FOLDER = join(abspath, "app/client/download")

    ALLOWED_EXTENSIONS = ['docx', 'pdf', 'txt']
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024


    #UPLOAD_FOLDER = "client/upload"
    #DOWNLOAD_FOLDER = "client/download"