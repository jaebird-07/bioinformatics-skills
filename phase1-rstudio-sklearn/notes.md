# Phase 1 — RStudio reactivation & revisiting the PFOA model

## Context
This dataset and modelling question come from a project I did during
Yonsei spring week. Here I rebuilt the data-handling layer by
hand — reading the six files, combining them, plotting, and summarising
with dplyr — to understand it properly with biological validation and context.

Doing this made clear *why* the earlier project used a global fit rather
than fitting each monkey separately: the dplyr summary showed how
unevenly the monkeys are sampled, and the plots showed a shared decay
shape with real spread between animals.

## Data
Six cynomolgus monkeys (Macaca fascicularis). Each file is digitised
serum concentration-time data for PFOA, taken from figures in the 2006
paper using WebPlotDigitizer. Two columns: time in days, concentration
in ug/mL. Between 5 and 10 points per monkey.

## What the plots showed
- All six monkeys follow the same overall pattern: concentration is
  highest early and falls as time goes on. This is the drug being cleared.
- The monkeys are not identical. At the same time point, concentrations
  differ by roughly 2-3x between animals. So there is real
  between-animal variation on top of the shared shape.
- The facet plot shows the same falling curve in every panel, just
  shifted up or down.

## What the summary table added
- The monkeys are sampled unevenly.
- Monkey 2054 is the weakest: only 6 points, first measurement on day 7,
  last on day 57. It misses both the early peak and the long tail.
- Monkey 2061 is the strongest: 10 points, first on day 2, followed out
  to day 123.

## Conclusion
- Some monkeys (2054 especially) do not have enough points over a long
  enough window to pin down their own curve.
- Fitting each monkey separately is therefore unreliable for all of them.
- Pooling all six into one combined ("global") fit uses every data point
  and gives a more stable estimate. That is the approach the earlier
  modelling work took.