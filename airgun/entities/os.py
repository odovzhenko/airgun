from navmazing import NavigateToSibling

from airgun.entities.base import BaseEntity
from airgun.navigation import BaseNavigator, navigator
from airgun.views.os import OperatingSystemView, OperatingSystemDetailsView


class OperatingSystemEntity(BaseEntity):

    def create_operating_system(self, values):
        view = self.navigate_to(self, 'New')
        view.fill(values)
        view.submit_data()

    def search(self, value):
        view = self.navigate_to(self, 'All')
        return view.search_element.search(value)


@navigator.register(OperatingSystemEntity, 'All')
class ShowAllOperatingSystems(BaseNavigator):
    VIEW = OperatingSystemView

    def step(self, *args, **kwargs):
        # TODO: No prereq yet
        self.view.navigation.select('Hosts', 'Operating systems')


@navigator.register(OperatingSystemEntity, 'New')
class AddNewOperatingSystem(BaseNavigator):
    VIEW = OperatingSystemDetailsView

    prerequisite = NavigateToSibling('All')

    def step(self, *args, **kwargs):
        self.view.browser.wait_for_element(
            self.parent.new, ensure_page_safe=True)
        self.parent.browser.click(self.parent.new)