## Task

> Please try to binarize several images, including the "blobs from FIJI" image, using various algorithms on the appropriate software (such as FIJI). Please provide a description of each algorithm's features and provide an example of an instance where the objects are challenging or impossible to extract after binarization.

| Algorithm                                         | Blobs from FIJI                                                             | Fukuoka castle tower                                                                | Ohori Park                                                                  |
| ------------------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Original                                          | ![blobs](/exercice-5-2-binarization/images/blobs.png)                       | ![fuku](/exercice-5-2-binarization/images/fukuoka-castle.jpg)                       | ![ohori](/exercice-5-2-binarization/images/ohori.jpg)                       |
| Fixed threshold                                   | ![blobs-fixed](/exercice-5-2-binarization/images/blobs-110.jpg)             | ![fuku-fixed](/exercice-5-2-binarization/images/fukuoka-castle-124.jpg)             | ![ohori-fixed](/exercice-5-2-binarization/images/ohori-120.jpg)             |
| Sauvola adaptative local threshold (radius of 15) | ![blobs-sauvola-15](/exercice-5-2-binarization/images/blobs-sauvola-15.png) | ![fuku-sauvola-15](/exercice-5-2-binarization/images/fukuoka-castle-sauvola-15.jpg) | ![ohori-sauvola-15](/exercice-5-2-binarization/images/ohori-sauvola-15.jpg) |
| Sauvola adaptative local threshold (radius of 50) | ![blobs-sauvola-50](/exercice-5-2-binarization/images/blobs-sauvola-50.png) | ![fuku-sauvola-50](/exercice-5-2-binarization/images/fukuoka-castle-sauvola-50.jpg) | ![ohori-sauvola-50](/exercice-5-2-binarization/images/ohori-sauvola-50.jpg) |
| Otsu adaptative local threshold (radius of 15)    | ![blobs-otsu-15](/exercice-5-2-binarization/images/blobs-otsu-15.png)       | ![fuku-otsu-15](/exercice-5-2-binarization/images/fukuoka-castle-otsu-15.jpg)       | ![ohori-otsu-15](/exercice-5-2-binarization/images/ohori-otsu-15.jpg)       |

I used the following algorithms:

- A fixed threshold algorithm (from the mini-test 5-1), in which I set the threshold by trial-and-error. As it is a global threshold algorithm, it is powerful when the image brightness level is gathered on one main peak in the histogram. This way we can divide the peak into two.

Let us look at the histograms of both the castle tower and the park:

| Castle tower                                                                    | Ohori Park                                                            | Blobs                                                                 |
| ------------------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| ![castle-histo](/exercice-5-2-binarization/images/fukuoka-castle-histogram.png) | ![ohori-histo](/exercice-5-2-binarization/images/ohori-histogram.png) | ![blobs-histo](/exercice-5-2-binarization/images/blobs-histogram.png) |

The castle tower image has 2-3 main brightness levels, it is easy to differentiate them, but we will have no contrast inside one of the peaks. It is unfortunate because we would like to see some contrast on the rocks which appear at the bottom of the image. On the contrary, the Ohori Park image has one main peak, and the parts of the image which have a wide range of gray within this peak can we somewhat clearly binarized. This is the reason why the shape of the water is nicely binarized, close from the camera. Finally, the Blobs image has one main dark peak, and a wide range of light-gray pixels, so the fixed threshold algorithm, just as the others, had no problem differientiating the dark pixels from the rest.

- Two adaptative, local thresholds algorithms:
  - Sauvola algorithm (with both a radius of 15 and a radius of 50)
  - Otsu algorithm (with a radius of 15)

> Note: I used FIJI for both of these algorithms.

After using the fixed threshold algorithm on the Castle Tower image, I wanted to use an algorithm that could show the contrast on the rocks at the bottom. I decided to use Otsu's algorithm, using a local threshold implementation. It did distinguish the bright and dark parts of the rocks by minimizing the variance between the classes of parts of the image. However, as expected by the algorithm's behaviour of course, it tried to do the same on the top part of the image, which is why the sky looks like mayhem. The behaviour is quite similar for the image of the Park.

Sauvola's algorithm showed the best results in my opinion, as it succeded to differentiate the pixel of the sky with the dark pixels of the tower, while also showing some contrast on the rocks. However, I couldn't manage to make a satisfying binarization of the Ohori Park image. This is mostly because the shades of gray were so close from each other.
