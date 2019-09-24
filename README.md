# Data Center API

A simple rest api that has an endpoint that calculates how many DevOps Enginers (DEs) are necessary (the minimum!), for a range of a Data Centers, as well as calculating which Data Center is best for a DM (DevOps Manager).

## How to run it (locally):
    $ python3 -m venv <venv_path>
    $ source <venv_path>/bin/activate
    $ pip install -r requirements.lock.txt
    $ cd src && python manange.py runserver

Open your browser at this link:

http://127.0.0.1:8000/load-impact/best-dc-setup?DM_capacity=12&DE_capacity=7&data_centers=[{"name": "Berlin", "servers": 11},{"name": "Stockholm", "servers": 21}]

(Select full link then copy/paste it on browser)


# MIT License

Copyright (c) [2019] [Nuno Diogo da Silva diogosilva.nuno@gmail.com]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.