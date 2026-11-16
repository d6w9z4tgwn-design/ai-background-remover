import argparse
from pathlib import Path

def output_path(source,folder): return Path(folder)/(Path(source).stem+'_transparent.png')
def main():
    p=argparse.ArgumentParser();p.add_argument('inputs',nargs='+');p.add_argument('--output',required=True);a=p.parse_args()
    from rembg import remove,new_session
    from PIL import Image
    folder=Path(a.output);folder.mkdir(parents=True,exist_ok=True);session=new_session('u2net')
    for source in a.inputs:
        dest=output_path(source,folder)
        if dest.exists(): raise FileExistsError(dest)
        with Image.open(source) as im: remove(im,session=session).save(dest)
if __name__=='__main__': main()
