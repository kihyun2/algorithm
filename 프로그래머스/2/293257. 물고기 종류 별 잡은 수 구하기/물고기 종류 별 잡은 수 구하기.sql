select count(*) as FISH_COUNT, b.FISH_NAME as FISH_NAME
from fish_info a join FISH_NAME_INFO b on a.fish_type = b.fish_type
group by fish_name
order by fish_count desc
