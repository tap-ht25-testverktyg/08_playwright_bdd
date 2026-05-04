import re

from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError
from playwright.sync_api import expect


@given(u'att vi är på sidan')
def step_impl(context):
    context.page.goto( context.base_url, timeout=5000 )


@when(u'användaren klickar på "Lägg till spelare"')
def step_impl(context):
    context.page.get_by_role("button", name="Lägg till spelare").click()


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

