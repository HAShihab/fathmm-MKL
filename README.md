# fathmm-MKL

Predicting the functional consequences of both coding and non-coding single nucleotide variants (see http://fathmm.biocompute.org.uk).

For more information, please refer to the following publication:

Shihab HA, Rogers MF, Gough J, Mort M, Cooper DN, Day INM, Gaunt TR, Campbell C (2014). An Integrative Approach to Predicting the Functional Consequences of Non-coding and Coding Sequence Variation. *Bioinformatics* (In Press)

## General Requirements

You will need the following packages installed on your system:

* ```tabix``` (included as part of this repository)
* ```Python``` (tested with Python 2.7)

## Running the Software

* Clone this repository

```
git clone https://github.com/HAShihab/fathmm-MKL
cd fathmm-MKL/
```

* Download our pre-computed database:

```
wget http://fathmm.biocompute.org.uk/database/fathmm-MKL_Current.tab.gz
```

**Note:** this database contains one-based coordinates (positions).  For true bed format (i.e. zero-based coordinates), please download the following database: http://fathmm.biocompute.org.uk/database/fathmm-MKL_Current_zerobased.tab.gz

* Add `tabix` to your PATH and create the database index file (*please be patient, this may take a while!*):

```
export PATH=./tabix-0.2.6/:$PATH
tabix -f -p bed fathmm-MKL_Current.tab.gz
```

* Run our script using the following command:

```
python fathmm-MKL.py <fin> <fo> <db>
```

In the above command, ```<fin>``` is the list of mutations to process (see ```test.txt``` for an example), ```<fo>``` is where the predictions are written and ```<db>``` is the pre-computed database downloaded in *Step 1*.

**Note:** the database index file must be created before running our script.  If this has not been created, your output will contain "No Prediction Found" for all variants!

## Prediction Interpretation

Predictions are given as *p*-values in the range [0, 1]: values above 0.5 are predicted to be deleterious, while those below 0.5 are predicted to be neutral or benign. *P*-values close to the extremes (0 or 1) are the highest-confidence predictions that yield the highest accuracy.

We use distinct predictors for positions either in coding regions (positions within coding-sequence exons) and non-coding regions (positions in intergenic regions, introns or non-coding genes). The coding predictor is based on 10 groups of features, labeled A-J; the non-coding predictor uses a subset of 4 of these feature groups, A-D (see our related publication for details on the groups and their sources).

**Note:** predictions based on a subset of features may not be as accurate as those based on complete feature sets. In particular, predictions that are missing the conservation score features (groups A and E) will tend to be less accurate than other predictions. To aid in interpreting these predictions, we provide a list of the feature groups that contributed to each prediction. 

## Genome Build

FATHMM-MKL predictions are based on GRCh37/hg19 genome build.

## Contributing:

We welcome any comments and/or suggestions that you may have regarding our software - please send an email to fathmm@biocompute.org.uk

