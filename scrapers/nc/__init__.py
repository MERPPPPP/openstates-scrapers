import lxml
from utils import State
from .people import NCPersonScraper
from .bills import NCBillScraper
from .events import NCEventScraper


class NorthCarolina(State):
    scrapers = {
        "people": NCPersonScraper,
        "bills": NCBillScraper,
        "events": NCEventScraper,
    }
    legislative_sessions = [
        {
            "_scraped_name": "1985-1986 Session",
            "classification": "primary",
            "identifier": "1985",
            "name": "1985-1986 Session",
            "start_date": "1985-02-05",
            "end_date": "1986-07-18",
        },
        {
            "_scraped_name": "1986 Special Session",
            "classification": "special",
            "identifier": "1985E1",
            "name": "1986 Special Session",
            "start_date": "1986-02-18",
            "end_date": "1986-06-05",
        },
        {
            "_scraped_name": "1987-1988 Session",
            "classification": "primary",
            "identifier": "1987",
            "name": "1987-1988 Session",
            "start_date": "1987-02-09",
            "end_date": "1988-07-12",
        },
        {
            "_scraped_name": "1989-1990 Session",
            "classification": "primary",
            "identifier": "1989",
            "name": "1989-1990 Session",
            "start_date": "1989-01-11",
            "end_date": "1990-07-28",
        },
        {
            "_scraped_name": "1989 Special Session",
            "classification": "special",
            "identifier": "1989E1",
            "name": "1989 Extra Session",
            "start_date": "1989-12-07",
            "end_date": "1989-12-07",
        },
        {
            "_scraped_name": "1990 Special Session",
            "classification": "special",
            "identifier": "1989E2",
            "name": "1990 Extra Session",
            "start_date": "1990-03-06",
            "end_date": "1990-03-06",
        },
        {
            "_scraped_name": "1991-1992 Session",
            "classification": "primary",
            "identifier": "1991",
            "name": "1991-1992 Session",
            "start_date": "1991-01-30",
            "end_date": "1992-07-25",
        },
        {
            "_scraped_name": "1991 Special Session",
            "classification": "special",
            "identifier": "1991E1",
            "name": "1991 Special Session",
            "start_date": "1991-12-30",
            "end_date": "1992-02-03",
        },
        {
            "_scraped_name": "1993-1994 Session",
            "classification": "primary",
            "identifier": "1993",
            "name": "1993-1994 Session",
            "start_date": "1993-01-27",
            "end_date": "1994-07-17",
        },
        {
            "_scraped_name": "1994 Special Session",
            "classification": "special",
            "identifier": "1993E1",
            "name": "1994 Special Session",
            "start_date": "1994-02-08",
            "end_date": "1994-03-26",
        },
        {
            "_scraped_name": "1995-1996 Session",
            "classification": "primary",
            "identifier": "1995",
            "name": "1995-1996 Session",
            "start_date": "1995-01-25",
            "end_date": "1996-06-21",
        },
        {
            "_scraped_name": "1996 1st Special Session",
            "classification": "special",
            "identifier": "1995E1",
            "name": "1996 Special Session 1",
            "start_date": "1996-02-21",
            "end_date": "1996-02-21",
        },
        {
            "_scraped_name": "1996 2nd Special Session",
            "classification": "special",
            "identifier": "1995E2",
            "name": "1996 Special Session 2",
            "start_date": "1996-07-08",
            "end_date": "1996-08-03",
        },
        {
            "_scraped_name": "1997-1998 Session",
            "classification": "primary",
            "identifier": "1997",
            "name": "1997-1998 Session",
            "start_date": "1997-01-29",
            "end_date": "1998-10-29",
        },
        {
            "_scraped_name": "1998 Special Session",
            "classification": "special",
            "identifier": "1997E1",
            "name": "1998 Special Session",
            "start_date": "1998-03-24",
            "end_date": "1998-05-11",
        },
        {
            "_scraped_name": "1999-2000 Session",
            "classification": "primary",
            "identifier": "1999",
            "name": "1999-2000 Session",
            "start_date": "1999-01-27",
            "end_date": "2000-07-13",
        },
        {
            "_scraped_name": "1999 Special Session",
            "classification": "special",
            "identifier": "1999E1",
            "name": "1999 Special Session",
            "start_date": "1999-12-15",
            "end_date": "1999-12-16",
        },
        {
            "_scraped_name": "2000 Special Session",
            "classification": "special",
            "identifier": "1999E2",
            "name": "2000 Special Session",
            "start_date": "2000-04-05",
            "end_date": "2000-04-05",
        },
        {
            "_scraped_name": "2001-2002 Session",
            "classification": "primary",
            "identifier": "2001",
            "name": "2001-2002 Session",
            "start_date": "2001-01-24",
            "end_date": "2002-11-13",
        },
        {
            "_scraped_name": "2002 Extra Session",
            "classification": "special",
            "identifier": "2001E1",
            "name": "2002 Extra Session on Redistricting",
            "start_date": "2002-05-14",
            "end_date": "2002-11-26",
        },
        {
            "_scraped_name": "2003-2004 Session",
            "classification": "primary",
            "identifier": "2003",
            "name": "2003-2004 Session",
            "start_date": "2003-01-29",
            "end_date": "2004-07-18",
        },
        {
            "_scraped_name": "2003 Extra Session",
            "classification": "special",
            "identifier": "2003E1",
            "name": "2003 Extra Session on Redistricting",
            "start_date": "2003-11-24",
            "end_date": "2003-11-25",
        },
        {
            "_scraped_name": "2003 Extra Session on Economic Development Issues",
            "classification": "special",
            "identifier": "2003E2",
            "name": "2003 Extra Session on Economic Development Issues",
            "start_date": "2003-12-09",
            "end_date": "2003-12-10",
        },
        {
            "_scraped_name": "2004 Extra Session",
            "classification": "special",
            "identifier": "2003E3",
            "name": "2004 Extra Session on Economic Development Issues",
            "start_date": "2004-11-04",
            "end_date": "2004-11-04",
        },
        {
            "_scraped_name": "2005-2006 Session",
            "classification": "primary",
            "identifier": "2005",
            "name": "2005-2006 Session",
            "start_date": "2005-01-26",
            "end_date": "2006-07-28",
        },
        {
            "_scraped_name": "2007-2008 Session",
            "classification": "primary",
            "identifier": "2007",
            "name": "2007-2008 Session",
            "start_date": "2007-01-24",
            "end_date": "2008-07-18",
        },
        {
            "_scraped_name": "2007 Extra Session",
            "classification": "special",
            "identifier": "2007E1",
            "name": "2007 Extra Session",
            "start_date": "2007-09-10",
            "end_date": "2007-09-11",
        },
        {
            "_scraped_name": "2008 Extra Session",
            "classification": "special",
            "identifier": "2007E2",
            "name": "2008 Extra Session",
            "start_date": "2008-03-20",
            "end_date": "2008-03-20",
        },
        {
            "_scraped_name": "2009-2010 Session",
            "classification": "primary",
            "identifier": "2009",
            "name": "2009-2010 Session",
            "start_date": "2009-01-28",
            "end_date": "2010-07-10",
        },
        {
            "_scraped_name": "2011-2012 Session",
            "classification": "primary",
            "identifier": "2011",
            "name": "2011-2012 Session",
            "start_date": "2011-01-26",
            "end_date": "2012-07-03",
        },
        {
            "_scraped_name": "2013-2014 Session",
            "classification": "primary",
            "identifier": "2013",
            "name": "2013-2014 Session",
            "start_date": "2013-01-30",
            "end_date": "2014-08-20",
        },
        {
            "_scraped_name": "2015-2016 Session",
            "classification": "primary",
            "identifier": "2015",
            "name": "2015-2016 Session",
            "start_date": "2015-01-30",
            "end_date": "2016-07-01",
        },
        {
            "_scraped_name": "2016 First Extra Session",
            "classification": "special",
            "identifier": "2015E1",
            "name": "2016 Extra Session 1",
            "start_date": "2016-02-18",
            "end_date": "2016-02-23",
        },
        {
            "_scraped_name": "2016 Second Extra Session",
            "classification": "special",
            "identifier": "2015E2",
            "name": "2016 Extra Session 2",
            "start_date": "2016-03-23",
            "end_date": "2016-03-23",
        },
        {
            "_scraped_name": "2016 Third Extra Session",
            "classification": "special",
            "identifier": "2015E3",
            "name": "2016 Extra Session 3",
            "start_date": "2016-12-13",
            "end_date": "2016-12-15",
        },
        {
            "_scraped_name": "2016 Fourth Extra Session",
            "classification": "special",
            "identifier": "2015E4",
            "name": "2016 Extra Session 4",
            "start_date": "2016-12-14",
            "end_date": "2016-12-19",
        },
        {
            "_scraped_name": "2016 Fifth Extra Session",
            "classification": "special",
            "identifier": "2015E5",
            "name": "2016 Extra Session 5",
            "start_date": "2016-12-21",
            "end_date": "2016-12-21",
        },
        {
            "_scraped_name": "2017-2018 Session",
            "classification": "primary",
            "identifier": "2017",
            "name": "2017-2018 Session",
            "start_date": "2017-01-11",
            "end_date": "2018-08-01",
        },
        {
            "_scraped_name": "2018 First Extra Session",
            "classification": "special",
            "identifier": "2017E1",
            "name": "2018 Extra Session 1",
            "start_date": "2018-07-24",
            "end_date": "2018-08-04",
        },
        {
            "_scraped_name": "2018 Second Extra Session",
            "classification": "special",
            "identifier": "2017E2",
            "name": "2018 Extra Session 2",
            "start_date": "2018-08-24",
            "end_date": "2018-08-27",
        },
        {
            "_scraped_name": "2018 Third Extra Session",
            "classification": "special",
            "identifier": "2017E3",
            "name": "2018 Extra Session 3",
            "start_date": "2018-10-02",
            "end_date": "2018-10-16",
        },
        {
            "_scraped_name": "2019-2020 Session",
            "classification": "primary",
            "identifier": "2019",
            "name": "2019-2020 Session",
            "start_date": "2019-01-03",
            "end_date": "2020-08-01",
        },
        {
            "_scraped_name": "2021-2022 Session",
            "classification": "primary",
            "identifier": "2021",
            "name": "2021-2022 Session",
            "start_date": "2021-01-04",
            # TODO: fix this when session ends
            "end_date": "2022-08-01",
        },
    ]
    ignored_scraped_sessions = []

    def get_session_list(self):
        from utils.lxmlize import url_xpath

        # This is the URL that populates the session `<select>` in the
        # state homepage header navigation
        return url_xpath(
            "https://webservices.ncleg.net/sessionselectlist/false", "//option/text()"
        )

    def extract_text(self, doc, data):
        doc = lxml.html.fromstring(data)
        text = " ".join(
            [x.text_content() for x in doc.xpath('//p[starts-with(@class, "a")]')]
        )
        return text
