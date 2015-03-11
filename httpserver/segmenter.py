#!/usr/bin/env python
# -*- coding: utf-8 -*-
# a wrapper for stanford nlp segment software

from __future__ import unicode_literals, print_function
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

import base
from comments import Comments
import config
import re

import tempfile
import os
import json
from subprocess import PIPE

# from nltk import compat
from nltk.internals import find_jar, config_java, java, _java_options

from nltk.tokenize.api import TokenizerI

class Segmenter(TokenizerI):

    def __init__(self):

        baseDir = config.STANFORD_PATH + config.SEGMENT
        dataDir = '%s/data' % baseDir
        classifier = '%s/pku.gz' % dataDir
        dicts = '%s/dict-chris6.ser.gz' % dataDir
        verbose = True
        _JAR = 'stanford-segmenter.jar'

        self._stanford_jar = find_jar(
            _JAR, baseDir + '/' + config.SEGMENT_JN,
            env_vars=(),
            searchpath=()
        )
        self._sihan_corpora_dict = dataDir
        self._model = classifier
        self._dict = dicts
        self._encoding = config.ENCODE_TYPE
        self.java_options='-mx2g'

        java_path = "/usr/lib/jvm/java-8/bin/java"
        os.environ['JAVAHOME'] = java_path

    def segment(self, tokens):
        return self.segment_sents(tokens)

    def segment_sents(self, sentences):
        """
        """
        encoding = self._encoding
        # Create a temporary input file
        _input_fh, self._input_file_path = tempfile.mkstemp(text=True)

        # Write the actural sentences to the temporary input file
        _input_fh = os.fdopen(_input_fh, 'wb')
        _input = '\n'.join((''.join(x) for x in sentences))
        # if isinstance(_input, compat.text_type) and encoding:
        #     _input = _input.encode(encoding)
        _input_fh.write(_input)
        _input_fh.close()

        cmd = [
            config.SEGMENT_CN,
            '-sighanCorporaDict', self._sihan_corpora_dict,
            '-textFile', self._input_file_path,
            '-sighanPostProcessing', 'true',
            '-keepAllWhitespaces', 'false',
            '-loadClassifier', self._model,
            '-serDictionary', self._dict
        ]

        stdout = self._execute(cmd)

        # Delete the temporary file
        os.unlink(self._input_file_path)

        return stdout

    def _execute(self, cmd, verbose=False):
        encoding = self._encoding
        cmd.extend(['-inputEncoding', encoding])

        default_options = ' '.join(_java_options)

        # Configure java
        config_java(options=self.java_options, verbose=verbose)

        stdout, _stderr = java(cmd, classpath=self._stanford_jar, stdout=PIPE, stderr=PIPE)

        # stdout = stdout.decode(encoding)

        # Return java configurations to their default values.
        config_java(options=default_options, verbose=False)

        return stdout


def segmenter(mid):

    # seg = Segmenter()

    # base.db.connect()

    print('segmenting...')

    command = '%s%s/segment.bat ctb ../data/%s.%s.200.utf-8 UTF-8 0 > ../data/%s.%s.segmented.utf-8' %\
              (config.STANFORD_PATH, config.SEGMENT, config.PREFIX, mid, config.PREFIX, mid)

    print(command)

    try:
        os.system(command)
    except(OSError):
        print('segmenting os error...')
    # sentences = []

    # for c in Comments:
    #     sentences.append(c.raw)

    # seged = seg.segment(sentences)
    # results = seged.split('\n')

    # iter = 0
    # for c in Comments:
    #     c.segmented = results[iter]
    #     c.save()
    #     iter += 1

    print('done...')

    # base.db.close()


if __name__ == '__main__':

    segmenter()
