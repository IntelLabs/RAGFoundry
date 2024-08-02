import logging

import hydra
from omegaconf import OmegaConf

from ragfoundry.processing.pipeline import DataPipeline

logger = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="./configs", config_name="processing")
def main(args):
    logger.info(OmegaConf.to_yaml(args))

    pipeline = DataPipeline(**args)
    pipeline.process()

    if args.hfhub_tag:
        pipeline.push_to_hub(args.hfhub_tag, private=True)


if __name__ == "__main__":
    main()
