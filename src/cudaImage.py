import sys
from timeit import default_timer as timer

import numpy as np
from numba import cuda, vectorize
#from numba.cuda import cufft
from scipy import misc, ndimage
from scipy.signal import fftconvolve


@vectorize(['complex64(complex64, complex64)'], target='gpu')
def vmult(a, b):
    return a * b


def best_grid_size(size, tpb):
    bpg = np.ceil(np.array(size, dtype=np.float) / tpb).astype(np.int).tolist()
    return tuple(bpg)


def main():
    laplacian_pts = '''
    -4 -1 0 -1 -4
    -1 2 3 2 -1
    0 3 4 3 0
    -1 2 3 2 -1
    -4 -1 0 -1 -4
    '''.split()

    laplacian = np.array(laplacian_pts, dtype=np.float32).reshape(5, 5)

    try:
        filename = sys.argv[1]
        image = ndimage.imread(filename, flatten=True).astype(np.float32)
    except IndexError:
        image = misc.lena().astype(np.float32)

    print("Image size: %s" % (image.shape,))

    response = np.zeros_like(image)
    response[:5, :5] = laplacian

    ts = timer()
    fftconvolve(image, laplacian, mode='same')
    te = timer()
    print('CPU: %.2fs' % (te - ts))

    threadperblock = 32, 8
    blockpergrid = best_grid_size(tuple(reversed(image.shape)), threadperblock)
    print('kernel config: %s x %s' % (blockpergrid, threadperblock))
    """
    cufft.FFTPlan(shape=image.shape, itype=np.complex64, otype=np.complex64)

    ts = timer()
    image_complex = image.astype(np.complex64)
    response_complex = response.astype(np.complex64)

    d_image_complex = cuda.to_device(image_complex)
    d_response_complex = cuda.to_device(response_complex)

    cufft.fft_inplace(d_image_complex)
    cufft.fft_inplace(d_response_complex)

    vmult(d_image_complex, d_response_complex, out=d_image_complex)

    cufft.ifft_inplace(d_image_complex)

    d_image_complex.copy_to_host().real / np.prod(image.shape)
    """
    te = timer()
    print('GPU: %.2fs' % (te - ts))


if __name__ == '__main__':
    main()
