import subprocess
from torchpack.utils.logging import logger
import argparse

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--dataset', type=str)
    # parser.add_argument('--name', type=str)
    # parser.add_argument('--space', type=str)
    # parser.add_argument('--nparams', type=int, nargs='+')
    # args = parser.parse_args()

    dataset = 'fashion'
    name = 'four0123'

    pres = ['python',
            'examples/eval.py',
            f'examples/configs/'
            f'{dataset}/{name}/eval/x2/real/opt2/300.yml',
            '--jobs=4',
            '--run-dir']

    # params = [7, 26, 15, 17]
    space = 'u3cu3_s0'
    mode = 'ldiff_blkexpand.blk8s1.1.1_diff7_chu10_sta40'

    with open(f"logs/x2/curve/{dataset}."
              f"{name}.noise.nonoise.0.6.0.7.0.8.0.9.txt",
              'a') as \
            wfid:

        for n_blk in [0.6, 0.7, 0.8, 0.9]:
            exp = f'runs/{dataset}.{name}.train.searched.scratch.x2.noise.' \
                  f'opt2.fix_nblk.blk{n_blk}.{space}.{mode}'

            logger.info(f"running command {pres + [exp]}")
            subprocess.call(pres + [exp], stderr=wfid)

        for n_blk in [0.6, 0.7, 0.8, 0.9]:
            exp = f'runs/{dataset}.{name}.train.searched.scratch.nonoise.' \
                  f'fix_nblk.blk{n_blk}.{space}.{mode}'

            logger.info(f"running command {pres + [exp]}")
            subprocess.call(pres + [exp], stderr=wfid)

