"""
INTRODUCTION

In today's exercise, we'll study one of the great failures of macroeconomics -
the Phillips Curve. Originally, this was the theory that unemployment and 
inflation were inversely related, so central banks could lower unemployment 
by increasing inflation (and vice-versa.) However, in the 1970s, this 
relationship broke down and the USA suffered both acute inflation
AND unemployment.
"""

"""
DOCUMENTATION

Below is the documentation for macrodata.csv; you don't have to read it 
thoroughly, merely consult it when the need arises or curiosity strikes.

Compiled by Skipper Seabold. All data are from the Federal Reserve Bank of St.
Louis [1] except the unemployment rate which was taken from the National
Bureau of Labor Statistics [2]. ::

    [1] Data Source: FRED, Federal Reserve Economic Data, Federal Reserve Bank of
        St. Louis; http://research.stlouisfed.org/fred2/; accessed December 15,
        2009.

    [2] Data Source: Bureau of Labor Statistics, U.S. Department of Labor;
        http://www.bls.gov/data/; accessed December 15, 2009.

    Number of Observations - 203

    Number of Variables - 14

    Variable name definitions::

        year      - 1959q1 - 2009q3
        quarter   - 1-4
        realgdp   - Real gross domestic product (Bil. of chained 2005 US$,
                    seasonally adjusted annual rate)
        realcons  - Real personal consumption expenditures (Bil. of chained
                    2005 US$, seasonally adjusted annual rate)
        realinv   - Real gross private domestic investment (Bil. of chained
                    2005 US$, seasonally adjusted annual rate)
        realgovt  - Real federal consumption expenditures & gross investment
                    (Bil. of chained 2005 US$, seasonally adjusted annual rate)
        realdpi   - Real private disposable income (Bil. of chained 2005
                    US$, seasonally adjusted annual rate)
        cpi       - End of the quarter consumer price index for all urban
                    consumers: all items (1982-84 = 100, seasonally adjusted).
        m1        - End of the quarter M1 nominal money stock (Seasonally
                    adjusted)
        tbilrate  - Quarterly monthly average of the monthly 3-month
                    treasury bill: secondary market rate
        unemp     - Seasonally adjusted unemployment rate (%)
        pop       - End of the quarter total population: all ages incl. armed
                    forces over seas
        infl      - Inflation rate (ln(cpi_{t}/cpi_{t-1}) * 400)
        realint   - Real interest rate (tbilrate - infl)
"""

"""
EXERCISE 1

Question: In the 1960s, was there an inverse relationship between unemployment
and inflation?

Long: Open macrodata.csv. What is the unit of observation?

Restrict your analysis to macroeconomics data between 1960-69 by creating a
smaller dataframe consisting entirely of data from this time period.

Using whatever package you prefer, perform a linear regression using Ordinary
Least Squares. Use umemployment as the dependant variable and inflation as the
independant variable. Was there a statistically significant relationship 
between these two variables? Is the coefficient positive or negative?
"""

"""
EXERCISE 2

Question: Did this relationship persist into the 1970s?

Long: Repeat Exercise 1 but with data from the period 1970-79. What is the
magnitude of the coefficient? How does it compare to the same coefficient from
the sixties? 

Hint: You don't have to use functions here - copy pasting code from Exercise 1 
is fine!
"""

"""
EXERCISE 3

Question: In the 1970s, what was the relationship between the annual CHANGE in 
inflation and unemployment?

Long: In your original dataframe, create a change in inflation column, subtracting
inflation in the current quarter with inflation from a year ago. (Be careful and
keep in mind the unit of observation of this data!) Then repeat Exercise 2 
using change in inflation instead of inflation.

Hint: For this exercise, you will have to use the shift() function. Run the 
following bit of code and explore the dataframe to get a sense of 
what shift() does:
    
    df["newvar"] = df["realint"].shift(1)
    
"""