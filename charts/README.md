#  Locust

locustのcluster構成をkubernets上に作ります。
locustのタスクのimageは別途作成しておいてください。

##  設定

|value|default|content|
|--------|---------|---|
|image|-|locust task docker image|
|slaveCount|10|slave count in parallel|
