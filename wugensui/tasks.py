import logging
import os
import subprocess

from celery import shared_task


logger = logging.getLogger(__name__)


@shared_task
def analyze_track():
    full_path = os.path.dirname(os.path.realpath(__file__))
    analyzer_path = os.path.join(full_path, 'analyze.out')
    logger.info("path: {}".format(analyzer_path))
    # subprocess.run([analyzer_path])
