# Warren

I did a lot of modeling for the group and used LIME and a model explainer to further understand how to make changes. I started with some initial EDA in the EDA notebook and looked at class balances. They were mostly even in the training and testing sets. Here is an example plot showing that:

![Class Balance](Images/classbalance].png)


In the model iterations notebook, I tested many different models for five epochs at a time. I slowly narrowed down a good set of layers and regularization to use thought there is still a lot of room for improvement.

I got LIME working in the notebook called Lime and made some fuctions to output explainers. 

In modelscoring, I evaluated every model that I had made and picked the one that performed the best. 

Last, colorcompmodels combines the best performing model with the color compressed images that Josh worked on. There were some more tweaks to the regularization to finalize the model. 