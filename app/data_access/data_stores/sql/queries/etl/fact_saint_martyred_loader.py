FACT_SAINT_MARTYRED_LOADER_QUERY: str = '''
TRUNCATE TABLE {saint_martyred_fact_table_name};

INSERT INTO {saint_martyred_fact_table_name} (year_of_death, age_at_death, region, martyred)
SELECT
	ranked_by_time.year_of_death,
	ranked_by_time.year_of_death - ranked_by_time.year_of_birth age_at_death,
	ranked_by_time.region,
	ranked_by_time.martyred
FROM
(SELECT
	id,
	active,
	year_of_birth,
	year_of_death,
	region,
	martyred,
	row_number() over(partition by id order by modified_date desc)
FROM
	{saint_lake_table_name}) ranked_by_time
WHERE ranked_by_time.active = true AND ranked_by_time.row_number = 1;
'''
