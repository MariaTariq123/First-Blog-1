# Copyright 2020 Google LLC
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

import os

from google.api_core.retry import Retry

import video_classification_create_model

PROJECT_ID = os.environ["GOOGLE_CLOUD_PROJECT"]
DATASET_ID = "VCN00000000000000000"
OPERATION_ID = None


@Retry()
def test_video_classification_create_model(capsys):
    try:
        video_classification_create_model.create_model(
            PROJECT_ID, DATASET_ID, "video_class_test_create_model"
        )
        out, _ = capsys.readouterr()
        assert "Dataset does not exist." in out
    except Exception as e:
        assert "Dataset does not exist." in e.message
