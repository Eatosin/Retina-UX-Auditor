# Methodology: The Physics of UI

Retina does not rely on subjective opinion. It relies on **Signal Processing**.

## 1. Visual Entropy (Clutter)
**Theory:** Shannon Entropy in information theory measures the amount of "surprise" or information in a signal. In UI, high entropy equates to visual clutter.
**Implementation:** 
$$ Clutter = \frac{\sum Edges_{canny}}{TotalPixels} $$
We use Canny Edge Detection to strip color and semantic meaning, isolating purely structural complexity.

## 2. Spectral Residual Saliency
**Theory:** The human brain is optimized to ignore redundant information (the background) and focus on the "Residual" (the unique object).
**Implementation:**
1.  Convert Image to Frequency Domain (FFT).
2.  Extract the Log-Spectrum.
3.  Subtract the Averaged Spectrum (Redundancy).
4.  Inverse FFT back to Spatial Domain.
**Result:** A heatmap predicting exactly where a user's eye will land in the first 500ms.

## 3. RMS Contrast
**Theory:** W3C/WCAG guidelines specify contrast ratios for text. Global Root Mean Square (RMS) contrast provides a heuristic for overall legibility.
**Implementation:** Standard Deviation of pixel intensities in the grayscale image.