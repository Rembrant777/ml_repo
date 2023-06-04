import hashlib
import os 
import shutil
import sys 
import tempfile

from urllib.request import urlopen, Request 
DOWNLOAD_BATCH_LENGTH = 1024 * 8 

# emma_notes: here try to import tqdm(process visual python library), 
# if tqdm is not installed, then create a fake backup tqdm 
try: 
    from tqdm.auto import tqdm # automatically select proper tqdm submodule if available 
except ImportError:
    # emma_notes: if import tqdm in current context failed, then create a fake tqdm 
    # that implements all its defined methods with simple, not complete implementation
    try:
        from tqdm import tqdm 
    except ImportError:
        # fake tqdm if it's not installed 
        class tqdm(object): # type: ignore 
            def __init__(self, total=None, disable=False,
                         unit=None, unit_scale=None, unit_divisor=None):
                self.total = total 
                self.disable = disable 
                self.n = 0
                # ignore unit, unit_scale, unit_divisor; they're just for real tqdm 
            
            def update(self, n):
                if self.disable:
                    return
                self.n += n
                # emma_notes: if total this member variable missing, then 
                # write err msg to sys.stderr, append error msg and flush 
                if self.total is None:
                    sys.stderr.write("\r{0:.1f} bytes".format(self.n))
                else:
                    sys.stderr.write("\r{0:.1f}%".format(100 * self.n / floag(self.total)))
                sys.stderr.flush()
            
            def __enter__(self):
                return self
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                if self.disable:
                    return 
                sys.stderr.write('\n')

def download_url_to_file(url, dst, hash_prefix=None, progress=True):
    r"""Download object at the given URL to a local path.
    Args:
        url (string): URL of the object to download
        dst (string): Full path where object will be saved, e.g. `/tmp/temporary_file`
        hash_prefix (string, optional): If not None, the SHA256 downloaded file should start with `hash_prefix`.
             hash_prefix default value is: None
        progress (bool, optional): whether or not to display a progress bar to stderr 
             progress default value is: True
    Example:
        >>> torch.hub.download_url_to_file('https://s3.amazonaws.com/pytorch/models/resnet18-5c106cde.pth', '/tmp/temporary_file')
    """
    file_size = None 
    # we use a different API for python2 since urllib(2) doesn't recognize the CA 
    # certificates in older Python 
    req = Request(url, headers={"User-Agent": "torch.hub"})
    u = urlopen(req)
    meta = u.info()
    if hasattr(meta, 'getheaders'):
        content_length = meta.getheaders("Content-Length")
    else:
        content_length = meta.get_all("Content-Length")
    # emma_notes: here check whether the fetch remote content is none or is empty
    # if not, then set the content_length to local variable file_size 
    if content_length is not None and len(content_length) > 0:
        file_size = int(content_length[0])
    
    # we deliberately save it in a temp file and move it after 
    # download is complete. this prevents a local working checkpoint 
    # being overridden by a broken download 
    dst = os.path.expanduser(dst)
    dst_dir = os.path.dirname(dst)
    f = tempfile.NamedTemporaryFile(delete=False, dir=dst_dir)

    try:
        if hash_prefix is not None:
            sha256 = hashlib.sha256() 
        # emma_note: here we begin to download remote file 
        # and call the tqdm to visual the downloading percentage progress
        # and the pbar is stand for (downloading) progress bar  
        with tqdm(total=file_size, disable=not progress,
                  unit='B', unit_scale=True, unit_divisor=1024) as pbar: 
            while True:
                # emma_note: every time we extract 8 * 1024 bytes from remote endpoint to local buffer 
                buffer = u.read(DOWNLOAD_BATCH_LENGTH)
                if len(buffer) == 0:
                    # emma_note: read finish break the loop 
                    break
                # emma_notes: every time after extracing specific bytes buffer from remote 
                # then write the buffer to local temporary file created by tmpfile.NamedTemporaryFile(...)
                f.write(buffer)
                # emma_notes: check function receives parameters 
                #    enable cryptographic of sha256(secure hash algorithm 256-bit) 
                #    if enabled, then append current remote fetched buffer to sha256
                if hash_prefix is not None:
                    sha256.update(buffer)
                # emma_notes: here call tqdm download progress visual library to append download progress 
                pbar.update(len(buffer))

            # emma_notes: after fetching all remote data and write to local tmp file close the file     
            f.close()

            # emma_notes: if sha256 is enabled verify it by calling hexdigest to verify 
            if hash_prefix is not None: 
                digest = sha256.hexdigest() 
                # emma_notes: value should be equal, otherwise throw an exception 
                if digest[:len(hash_prefix)] != hash_prefix:
                    raise RuntimeError('invalid hash value (expected "{}", got "{}")'
                                       .format(hash_prefix, digest))
            
            # emma_notes: after checking everything is done, move the temporary file to given 
            # destination file
            shutil.move(f.name, dst)
    finally:
        # emma_notes: in finally block double check the temporary file is removed from system 
        f.close()
        if os.path.exists(f.name):
            os.remove(f.name)        

