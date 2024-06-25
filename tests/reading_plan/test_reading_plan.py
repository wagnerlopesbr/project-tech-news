from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import patch


support = "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy"


def test_reading_plan_group_news():
    mocked_news = [
        {"title": "News 1", "reading_time": 4},
        {"title": "News 2", "reading_time": 3},
        {"title": "News 3", "reading_time": 10},
        {"title": "News 4", "reading_time": 15},
        {"title": "News 5", "reading_time": 12},
    ]
    with patch(support, return_value=mocked_news):
        with pytest.raises(
            ValueError,
            match="Valor 'available_time' deve ser maior que zero"
        ):
            ReadingPlanService.group_news_for_available_time(0)
        result = ReadingPlanService.group_news_for_available_time(10)
        expected_result = {
            "readable": [
                {
                    "unfilled_time": 3,
                    "chosen_news": [
                        ("News 1", 4),
                        ("News 2", 3),
                    ],
                },
                {
                    "unfilled_time": 0,
                    "chosen_news": [
                        ("News 3", 10),
                    ],
                },
            ],
            "unreadable": [
                ("News 4", 15),
                ("News 5", 12),
            ],
        }
        assert result == expected_result
