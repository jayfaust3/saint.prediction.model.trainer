MARTYRED_QUERY: str = '''
    SELECT
	    year_of_death,
	    age_at_death,
	    region,
	    martyred AS target
    FROM
	    public.fact_saint_martyred;
'''
