#!/bin/bash
nikola build
rsync -a output/ biao@gms.cs.unc.edu:/afs/cs.unc.edu/project/geom/public_html/ClothM


