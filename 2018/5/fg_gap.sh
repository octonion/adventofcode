#!/bin/sh

gap -r -b -q free_group.g << EOI
Length(outcome(data));
quit;
EOI
