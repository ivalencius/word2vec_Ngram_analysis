# R_nGram_analysis
Project to train [word2vec](https://jalammar.github.io/illustrated-word2vec/) models based upon the [Google nGram corpus](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html). Data was downloaded and sorted (very inefficiently) according to [this repo](https://github.com/ivalencius/nGram_download_and_sort).

## Layout
* [Training.Rmd](https://github.com/ivalencius/R_nGram_analysis/blob/main/Training.Rmd) → File to train word2vec models. Models will be stored in /Models/ but are to large to upload to GitHub.
* [Investigation.Rmd](https://github.com/ivalencius/R_nGram_analysis/blob/main/Investigation.Rmd) → File to open and examine trained word2vec models.
* [Model_info](https://github.com/ivalencius/R_nGram_analysis/blob/main/Model_info.xlsx) → Information regarding the location of data on the SSD as well as metadata regarding the trained word2vec models.



