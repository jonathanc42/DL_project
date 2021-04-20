import json
import os
import datasets

_CITATION = '''\
    author = {Wu, Qiyuan},
    year = {2021}
'''

_DESCRIPTION = '''\
    TAPT ChemProt data loader
'''

_TASK = 'chemprot'

class TaskConfig(datasets.BuilderConfig):

    def __init__(self, **kwargs):
        super(TaskConfig, self).__init__(**kwargs)

class TaskDataset(datasets.GeneratorBasedBuilder):
    _TRAIN_FILE = _TASK + '_train.jsonl'
    _TEST_FILE = _TASK + '_test.jsonl'
    _VAL_FILE = _TASK + '_dev.jsonl'

    BUILDER_CONFIGS = [
        TaskConfig(
            name='task',
            version=datasets.Version('1.0.0'),
            description='TAPT dataset loader',
        ),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    'text': datasets.Value('string'),
                    'labels': datasets.features.ClassLabel(names=['INHIBITOR',
                                                                'SUBSTRATE_PRODUCT-OF',
                                                                'DOWNREGULATOR',
                                                                'SUBSTRATE',
                                                                'INDIRECT-UPREGULATOR',
                                                                'AGONIST-INHIBITOR',
                                                                'AGONIST',
                                                                'INDIRECT-DOWNREGULATOR',
                                                                'UPREGULATOR',
                                                                'PRODUCT-OF',
                                                                'AGONIST-ACTIVATOR',
                                                                'ACTIVATOR',
                                                                'ANTAGONIST'])
                }
            ),
            supervised_keys=None,
            homepage='',
            citation=_CITATION,
        )
    
    def _split_generators(self, dlmanager):
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN, gen_kwargs={'filepath': os.path.join('data', self._TRAIN_FILE)}
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION, gen_kwargs={'filepath': os.path.join('data', self._VAL_FILE)}
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST, gen_kwargs={'filepath': os.path.join('data', self._TEST_FILE)}
            ),
        ]
    
    def _generate_examples(self, filepath):
        with open(filepath, encoding="utf8") as f:
            for id_, line in enumerate(f):
                data = json.loads(line)
                text = data['text']
                label = data['label']
                yield id_, {'text': text, 'labels': label}