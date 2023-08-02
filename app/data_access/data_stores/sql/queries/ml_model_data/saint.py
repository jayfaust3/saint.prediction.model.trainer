MARTYRED_QUERY: str = '''
    SELECT
	    year_of_death,
	    age_at_death,
	    region,
	    martyred AS target
    FROM
	    {saint_martyred_fact_table_name};
'''
