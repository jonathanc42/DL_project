DATASETS = {
    "chemprot": {
        "data_dir": "https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/chemprot/",
        "dataset_size": 4169
    },
    "rct-20k": {
        "data_dir": "https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/rct-20k/",
        "dataset_size": 180040
    },
    "rct-sample": {
        "data_dir": "https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/rct-sample/",
        "dataset_size": 500
    },
    "citation_intent": {
        "data_dir": "https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/citation_intent/",
        "dataset_size": 1688
    },
    "sciie": {
        "data_dir": "https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/sciie/",
        "dataset_size": 3219
    },
    "ag": {
        "data_dir": "https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/ag/",
        "dataset_size": 115000
    },
    "hyperpartisan_news": {
        "data_dir": "https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/hyperpartisan_news/",
        "dataset_size": 500
    },
    "imdb": {
        "data_dir": "https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/imdb/",
        "dataset_size": 20000
    },
    "amazon": {
        "data_dir": "https://allennlp.s3-us-west-2.amazonaws.com/dont_stop_pretraining/data/amazon/",
        "dataset_size": 115251
    }
}

if __name__ == '__main__':
    import requests
    import os
    for k, v in DATASETS.items():
        urls = []
        print('downloading', k)
        urls.append(v['data_dir'] + 'train.jsonl')
        urls.append(v['data_dir'] + 'dev.jsonl')
        urls.append(v['data_dir'] + 'test.jsonl')

        for url in urls:
            r = requests.get(url, allow_redirects=True)
            with open(k + '_' + os.path.split(url)[-1], 'wb') as f:
                f.write(r.content)
