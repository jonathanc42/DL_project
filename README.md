# DL_project

## Projcet Meta

### Team: More Than Meets the Eye

### Facebook Project: Yes

### Project Title: Transformer Adapter Capstone Project

### Project Summary:

Pre-trained Transformer language models achieve strong performance on many NLP tasks. However, in multi-task application, fine-tuning models and storing weights for each task can be quite challenging. For large models, there could be billions of parameters (Pfeiffer et al., 2020) needed to be fine-tuned. Adding adapter modules in the transformer model can potentially solve this problem. Adapter modules are introduced as an alternative lightweight fine-tuning strategy and yield a compact and extensible model. They add only a few trainable parameters per task, and new tasks can be added without revisiting previous ones (Houlsby et al., 2019). We would like to create adapters for transformer model and compare the performance with advanced fine-tuning alone. We want to understand how the adapter module can improve the efficiency and discover more benefits of using the adapters.


### Approach:

•	We will first apply transfer learning to finetune a base distilbert model for each individual task. Choosing the distilbert based on the lean resources it requires, and can also cross validate the result on RoBERTa in the paper.

•	We will then build transformer adapter model with distilbert and then compare it with the fine-tuning models. As the result shown in Gururangan et al. (2020), we expect to reproduce and prove the domain-adaptive pretraining leads to performance gains. We plan to proceed to TAPT first for time concern.

•	As a stretch goal, we want to research the disadvantages and potential limitation of the adaptive model.

### Resources/Related Work:
[1] Suchin Gururangan, Ana Marasović, Swabha Swayamdipta, Kyle Lo, Iz Beltagy, Doug Downey, Noah A.Smith, “Don't Stop Pretraining: Adapt Language Models to Domains and Tasks“, In ACL 2020.

[2] Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin de Laroussilhe, Andrea Gesmundo, Mona Attariyan, Sylvain Gelly, “Parameter-Efficient Transfer Learning for NLP”, In ICML 2019.

[3] Jonas Pfeiffer, Andreas Rücklé, Clifton Poth, Aishwarya Kamath, Ivan Vulić, Sebastian Ruder, Kyunghyun Cho, Iryna Gurevych, “AdapterHub: A Framework for Adapting Transformers”, arXiv preprint.

[4] https://course.fast.ai/#using-a-gpu

[5] https://adapterhub.ml/

[6] https://huggingface.co/transformers/

[7] https://towardsdatascience.com/transformers-retraining-roberta-base-using-the-roberta-mlm-procedure-7422160d5764

[8] https://huggingface.co/blog/how-to-train

### Datasets:

Kaggle arXiv dataset

https://github.com/allenai/dont-stop-pretraining#downloading-data
```bash
curl https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/chemprot/train.jsonl -o ./data/train.jsonl
curl https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/chemprot/dev.jsonl -o ./data/dev.jsonl
curl https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/chemprot/test.jsonl -o ./data/test.jsonl
```
### Team Members:

Zhongshui Cao

Qiyuan Wu

Yiyun Zhang

### Looking for more members:
No
