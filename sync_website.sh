#!/bin/bash
nikola build
rsync -a output/ biao@gms.cs.unc.edu:public_html/

