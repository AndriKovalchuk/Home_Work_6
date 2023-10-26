import sys
from pathlib import Path

JPEG_IMAGES = []
PNG_IMAGES = []
JPG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
ARCHIVES = []

REGISTER_EXTENSIONS = {'JPEG': JPEG_IMAGES,
                       'PNG': PNG_IMAGES,
                       'JPG': JPG_IMAGES,
                       'SVG': SVG_IMAGES,
                       'AVI': AVI_VIDEO,
                       'MP4': MP4_VIDEO,
                       'MOV': MOV_VIDEO,
                       'MKV': MKV_VIDEO,
                       'DOC': DOC_DOCUMENTS,
                       'DOCX': DOCX_DOCUMENTS,
                       'TXT': TXT_DOCUMENTS,
                       'PDF': PDF_DOCUMENTS,
                       'XLSX': XLSX_DOCUMENTS,
                       'PPTX': PPTX_DOCUMENTS,
                       'MP3': MP3_AUDIO,
                       'OGG': OGG_AUDIO,
                       'WAV': WAV_AUDIO,
                       'AMR': AMR_AUDIO,
                       'ZIP': ARCHIVES,
                       'GZ': ARCHIVES,
                       'TAR': ARCHIVES}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN_EXTENSIONS = set()


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        extension = get_extension(item.name)
        full_name = folder / item.name
        if not extension:
            pass
        else:
            try:
                ext_reg = REGISTER_EXTENSIONS[extension]
                ext_reg.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN_EXTENSIONS.add(extension)


if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan(Path(folder_process))

    print(f'FOLDERS: {FOLDERS}')

    print(f'Images JPEG: {JPEG_IMAGES}')
    print(f'Images PNG: {PNG_IMAGES}')
    print(f'Images JPG: {JPG_IMAGES}')
    print(f'Images SVG: {SVG_IMAGES}')

    print(f'Video AVI: {AVI_VIDEO}')
    print(f'Video MP4: {MP4_VIDEO}')
    print(f'Video MOV: {MOV_VIDEO}')
    print(f'Video MKV: {MKV_VIDEO}')

    print(f'Documents DOC: {DOC_DOCUMENTS}')
    print(f'Documents DOCX: {DOCX_DOCUMENTS}')
    print(f'Documents TXT: {TXT_DOCUMENTS}')
    print(f'Documents PDF: {PDF_DOCUMENTS}')
    print(f'Documents XLSX: {XLSX_DOCUMENTS}')
    print(f'Documents PPTX: {PPTX_DOCUMENTS}')

    print(f'Audio MP3: {MP3_AUDIO}')
    print(f'Audio OGG: {OGG_AUDIO}')
    print(f'Audio WAV: {WAV_AUDIO}')
    print(f'Audio AMR: {AMR_AUDIO}')

    print(f'EXTENSIONS: {EXTENSIONS}')
    print(f'UNKNOWN_EXTENSIONS: {UNKNOWN_EXTENSIONS}')
