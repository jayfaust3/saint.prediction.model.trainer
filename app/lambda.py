import logging
from http import HTTPStatus
from json import dumps
from ..container import Container
from ..application.ml_model_trainers.saint.martyred import MartyredModelTrainer


def handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    try:
        di_container = Container()

        martyred_model_trainer: MartyredModelTrainer = di_container.martyred_model_trainer

        martyred_model_trainer.train_model()

    except Exception as e:
        logger.error(e, exc_info=True)

        return {
            'statusCode': HTTPStatus.INTERNAL_SERVER_ERROR,
            'message': dumps(e)
        }

    return {
        'statusCode': HTTPStatus.OK,
        'message': dumps({
            'event': event,
            'context': context
        })
    }
