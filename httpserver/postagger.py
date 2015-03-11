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

class PosTagger(TokenizerI):

    def __init__(self):

        baseDir = config.STANFORD_PATH + config.POSTAG
        verbose = True
        _JAR = 'stanford-postagger.jar'

        self._stanford_jar = find_jar(
            _JAR, baseDir + '/' + config.POSTAG_JN,
            env_vars=(),
            searchpath=()
        )
        self._model = '%s/models/chinese-distsim.tagger' % baseDir
        self.java_options='-mx2g'
        self._encoding = config.ENCODE_TYPE

        java_path = "/usr/lib/jvm/java-8/bin/java"
        os.environ['JAVAHOME'] = java_path

    def postag(self, tokens):
        return self.postag_sents(tokens)

    def postag_sents(self, sentences):
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
            config.POSTAG_CN,
            '-model', self._model,
            '-textFile', self._input_file_path
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

        stdout, _stderr = java(cmd,classpath=self._stanford_jar, stdout=PIPE, stderr=PIPE)

        # stdout = stdout.decode(encoding)

        # Return java configurations to their default values.
        config_java(options=default_options, verbose=False)

        return stdout


def postagger(mid = 1):

    # pt = PosTagger()

    # base.db.connect()

    # sentences = []

    print('pos tagging...')

    baseDir = '%s%s/' % (config.STANFORD_PATH, config.POSTAG)
    prefix = '%s.%s.' % (config.PREFIX, mid)

    command = '%sstanford-postagger.bat %smodels/chinese-distsim.tagger ../data/%ssegmented.clean.utf-8 > ../data/%spostagged.utf-8' %\
              (baseDir, baseDir, prefix, prefix)

    try:
        os.system(command)
    except(OSError):
        print('segmenting os error...')

    # for c in Comments:
    #     sentences.append(c.segmented)

    # tagged = pt.postag(sentences)

    # results = tagged.split('\n')

    # iter = 0
    # for c in Comments:
    #     c.posed = results[iter]
    #     c.save()
    #     iter += 1

    print('done...')

    # base.db.close()


if __name__ == '__main__':

    postagger()
