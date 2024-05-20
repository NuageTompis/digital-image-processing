## Task one

> Please describe the feature of the below Fourier transform from the below image.

| Original image                                                   | Fourier transform                                              |
| ---------------------------------------------------------------- | -------------------------------------------------------------- |
| ![original](/11-in-class-practice-questions/images/original.png) | ![fourier](/11-in-class-practice-questions/images/fourier.png) |

First of all, we can note that the points near the center of the Fourier transform have a high intensity, which denotes the fact that the original image is mainly composed of low-frequency components in the Fourier domain. This is a typical trait of human-made images, as they tend to have a lot of smooth regions, such as the shoulder or the hat here, as well as the background. The low-frequency components are responsible for the main color and shape of the image.

We can also see bright horizontal and vertical lines on the axis *y=0* and *x=0*, as well as a subtle diagonal line from the top-left to the bottom-right corners. These lines depict more details (edges and rapid brightness change) on horizontal and vertical axis of the images. Part of the images that are likely responsible for this include the lips (horizontal), and the hair on the right of the image. The hat is probably responsible for the components in the diagonal of the Fourier transform.

## Task two

> Please describe the upper image analysis by using technical terms, 
convolution, multiplying, and Fourier transform.

| Domain  | Original                                                         | Filter                                                         | Filtered                                                                 |
| ------- | ---------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Image   | ![alt text](/11-in-class-practice-questions/images/original.png) | N/A                                                            | ![alt text](/11-in-class-practice-questions/images/filtered.png)         |
| Fourier | ![alt text](/11-in-class-practice-questions/images/fourier.png)  | ![alt text](/11-in-class-practice-questions/images/filter.png) | ![alt text](/11-in-class-practice-questions/images/fourier-filtered.png) |

The previous operation consists of a blur of the original image. We can see the original image as well as its Fourier transform, then we apply a convolution filter by multiplying the image in the Fourier domain by an object with low-frequency components only. This effectively only select the low-frequency components of the original image, it is a product in the Fourier domain and a convolution in the image domain. The resulting image (in the image domain) is a blurred version of the original one, where details and sharp edges, corresponding to high-frequency components, have been eliminated.

## Task 3

> Please describe compression algorithms on JEPG by noting the 
feature of these images.

| Image 1                                                    | Image 2                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- |
| ![jpeg1](/11-in-class-practice-questions/images/jpeg1.png) | ![jpeg2](/11-in-class-practice-questions/images/jpeg2.png) |

The JPEG compression method uses a Dicrete Cosine Transform (DCT) to convert the image into a combination of cosine patterns. The process uses block division, and it is possible to choose the aspect ratio to choose balance size and quality. Because of this, artifacts such as block noise appear (as in image 1). Image 2 has a higher aspect ratio and these effects are not visible.

Before performing the DCT however, the channels of the image (Red, Green and Blue) are converted to another color space, more meaningful to the human eye, which is the *YCbCr* space.

## Task 4

> Please plan an alogrithms to extract the numeric 90413.

| Original image                                                             |
| -------------------------------------------------------------------------- |
| ![hidden-number](/11-in-class-practice-questions/images/hidden-number.png) |

To tackle this problem, I first applied a Gaussian blur filter to try to reduce the influence of the noise, which is abundant in the image.

I then binarized the image using a local threshold algorithm (namely the Phansalkar algorithm), which I then skeletonized, all of this using Fiji.

I should note that, after binarization the number *9* is barely readable for the human eye, I did not manage to obtain a better result so I deciced to focus on the remaining digits. After skeletonization the number *9* in unredeable even for the human eye, but the others are still fairly easy to recognize.

| Blurred                                                       | Binarized                                                              | Skeletonized                                                        | Cropped                                                           |
| ------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------- |
| ![hidden](/11-in-class-practice-questions/images/hn-blur.png) | ![binary](/11-in-class-practice-questions/images/hn-phansalkar-25.png) | ![skeleton](/11-in-class-practice-questions/images/hn-skeleton.png) | ![cropped](/11-in-class-practice-questions/images/hn-cropped.png) |

I tried to use multiple methods to extract the numbers from the skeletonized image, but none of them worked. So I deciced to crop the interesting part only (including the 9).

Finally, I used an online *text recognition* tool that you may find [here](https://text-scan.com/), and this is what I obtain: `SO 41-3`.

Even though it is not exactly the expected result, I think it is quite close (the letter *S* does share similarities with the number *9*) and the capital letter *O* is almost a zero. Maybe if I had used a model that looks for digits only I would have had the correct result.