# -*- coding: utf-8 -*-
#
# Copyright 2018 - Swiss Data Science Center (SDSC)
# A partnership between École Polytechnique Fédérale de Lausanne (EPFL) and
# Eidgenössische Technische Hochschule Zürich (ETHZ).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Custom console echo."""

import os

import click


def echo_via_pager(*args, **kwargs):
    """Display pager only if it does not fit in one terminal screen.

    NOTE: The feature is available only on ``less``-based pager.
    """
    try:
        restore = 'LESS' not in os.environ
        os.environ.setdefault('LESS', '-F')
        click.echo_via_pager(*args, **kwargs)
    finally:
        if restore:
            os.environ.pop('LESS', None)
