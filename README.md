# fathmm-MKL

Predicting the functional consequences of both coding and non-coding single nucleotide variants (see http://fathmm.biocompute.org.uk).

For more information, please refer to the following publication:

Shihab HA, Rogers MF, Gough J, Mort M, Cooper DN, Day INM, Gaunt TR, Campbell C (2014). An Integrative Approach to Predicting the Functional Consequences of Non-coding and Coding Sequence Variation. *Bioinformatics* (In Press)

## General Requirements

You will need the following packages installed on your system:

* ```tabix``` (included as part of this repository)
* ```Python``` (tested with Python 2.7)

## Running the Software

* Download our pre-computed database:

```
wget http://fathmm.biocompute.org.uk/database/fathmm-MKL_Current.tab.gz
```

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

## Contributing:

We welcome any comments and/or suggestions that you may have regarding our software - please send an email to fathmm@biocompute.org.uk

