select count(*) as fish_type, max_length, fish_type
from fish_info
group by fish_type
order by fish_type asc;