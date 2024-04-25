select count(*) as FISH_COUNT
from FISH_INFO
where length < 10 OR length is null