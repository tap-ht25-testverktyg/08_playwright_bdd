import re

from behave import given, when, then
from playwright.sync_api import expect

from src.features.pages.main_page import MainPage


@given(u'att vi är på sidan')
def step_impl(context):
    context.main = MainPage(context.base_url, context.page)
    context.main.navigate()


@when(u'användaren klickar på "Lägg till spelare"')
def step_impl(context):
    context.main.click_add_player_button()


@when(u'användaren skriver "{player}"')
def step_impl(context, player):
    # välj ut input-elementet som har id "player-name"
    input_element = context.page.locator("#player-name")
    input_element.fill(player)


@then(u'spelaren "{player}" visas i listan över spelare')
def step_impl(context, player):
    # alla gröna rutor med CSS-klassen "player" som innehåller spelarens namn
    all_players = context.page.locator(".player")
    this_player = all_players.get_by_text(re.compile(player))
    # tänk på: hur kan vi säkra systemet för användare som använder specialtecken? (t.ex. ?.*[])
    expect(this_player).to_be_visible()

