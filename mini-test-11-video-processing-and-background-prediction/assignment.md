## Problem wording

> Suppose we have a 10-valued image from 0-9. Now, if we extracted pixel values at a pixel in time, we observed the following pixel value changes  
> 
> `0 1 2 1 2 1 0 2 1 8 1 3 0`
> 
> Describe the overviews of Bayesian estimation of background, i.e., If the initial prior probability that a pixel with a value between 0 and 9 is a background or a moving object is 0.5, how does the posterior probability of a background with that pixel's value change? And when the pixel has a value of 8, it is abnormal and can be considered to have been crossed by a moving object.
> 
> If possible, calculate and describe the posterior probability for each time step of a value.

## Background probability

Since we do not have access to the image histogram, we will consider the pixel values that we have to estimate the probability that a background pixel has a brightness value I.

| Pixel value | Occurences |
| ----------- | ---------- |
| 0           | 3          |
| 1           | 5          |
| 2           | 3          |
| 3           | 1          |
| 8           | 1          |
| Total       | 13         |

Using the class material's notations, we have:

- $p(I=0|\omega_0) = \frac{3}{13}$
- $p(I=1|\omega_0) = \frac{5}{13}$
- $p(I=2|\omega_0) = \frac{3}{13}$
- $p(I=3|\omega_0) = \frac{1}{13}$
- $p(I=8|\omega_0) = \frac{1}{13}$
- $p(I\in\{4,5,6,7,9\}|\omega_0) = 0$

Using the same logic as the class material, we always have $p(I|\omega_1) = \frac{1}{10}$, for every value of I.

## Posterior probability computation

We shall note the probability at frame *n* in [1,13] of the pixel being part of a background object knowing its brightness value as $p_n(\omega_0|I)$

Using the class material's formula, we have:

$p_1(\omega_0|I=0) = \frac{p(I=0|\omega_0)*p_1(\omega_0)}{p_1(\omega_0)*p(I=0|\omega_0)+p_1(\omega_1)*p(I=0|\omega_1)}$

We will also use the formula: $p_1(\omega_0) = p_0(\omega_1|I)$, where $p_0(\omega_1|I)=\frac{1}{2}$ for each I as the problem states. We also have: $p_0(\omega_0|I)=\frac{1}{2}$.

This gives us:

$p_1(\omega_0|I=0) = \frac{\frac{3}{13}*\frac{1}{2}}{\frac{1}{2}*\frac{3}{13}+\frac{1}{2}*\frac{1}{10}} = 30/43 \approx 0.7$

`The probability that the pixel is part of a moving object in the first frame is thus estimated at 30%.`

Let us now make the calculus for the second frame:

$p_2(\omega_0|I=1) = \frac{p(I=1|\omega_0)*p_2(\omega_0)}{p_2(\omega_0)*p(I=1|\omega_0)+p_2(\omega_1)*p(I=1|\omega_1)} = p_1(\omega_0|I=0) = \frac{\frac{5}{13}*\frac{30}{43}}{\frac{30}{43}*\frac{5}{13}+\frac{13}{43}*\frac{1}{10}} = \frac{1500}{1669} \approx0.9$

`The probability that the pixel is part of a moving object in the second frame is thus estimated at 10%.`

I obtain the following probabilities, for each frame, that the pixel is part of a moving object (in percentage):

| Frame | Probability |
| ----- | ----------- |
| 1     | 30.2325     |
| 2     | 10.1258     |
| 3     | 4.6549      |
| 4     | 1.2534      |
| 5     | 0.5470      |
| 6     | 0.1428      |
| 7     | 0.0619      |
| 8     | 0.0268      |
| 9     | 0.0069      |
| 10    | 0.0090      |
| 11    | 0.0023      |
| 12    | 0.0030      |
| 13    | 0.0013      |

Something unusual happens at frame 10 (when the pixel brightness value is 8), as the probability increases suddenly.

However, the probability remains very low, so I suspect that I have made an error of the model is not sufficient.