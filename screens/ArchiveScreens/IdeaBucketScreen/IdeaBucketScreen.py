from kivy.uix.screenmanager import Screen
from objects.IdeaBucket import IdeaBucket
from kivy.uix.treeview import TreeView, TreeViewLabel
import re
ideaBucket = IdeaBucket()



class IdeaBucketScreen(Screen):
    selectedNode = None
    selectedTag = None
    selectedIdea = None

    def refresh_idea_tree(self):
        for node in [i for i in self.ids.ideaBucketTreeView.iterate_all_nodes()]:
            self.ids.ideaBucketTreeView.remove_node(node)
        self.ids.ideaBucketTreeView.bind(selected_node=self.on_node_selected)
        for tag in ideaBucket.tags:
            tree_node = self.ids.ideaBucketTreeView.add_node(TreeViewLabel(text=tag['name']))

            counter = 0

            for idea in ideaBucket.ideas:
                if(idea['tag'] == tag['name']):
                    self.ids.ideaBucketTreeView.add_node(TreeViewLabel(text=idea['name']), tree_node)
                    counter += 1

            tree_node.text += f' ({counter})'
        
    def on_node_selected(self, treeview, node):
        self.selectedNode = node
        if node != self.ids.ideaBucketTreeView.root:
            parent_node = None
            for child_node in self.ids.ideaBucketTreeView.iterate_all_nodes():
                if node in child_node.nodes:
                    parent_node = child_node
                    break
            if(parent_node == self.ids.ideaBucketTreeView.root):
                text = node.text
                node_text = re.findall(r'(.+)\s+\(\d+\)', text)[0]
                self.selectedTag = node_text
                self.selectedIdea = None
                self.ids.tagNameInput.text = node_text
                self.clear_idea_button_clicked()
            else:
                self.selectedTag = None
                self.selectedIdea = node.text

                

                for idea in ideaBucket.ideas:
                    if(idea['name'] == node.text):
                        self.ids.ideaNameInput.text = idea['name']
                        self.ids.ideaDescriptionInput.text = idea['description']
                        self.ids.tag_spinner.text = idea['tag']
                        self.ids.tag_spinner.values = [tag['name'] for tag in ideaBucket.tags]
                        self.clear_tag_button_clicked()

    def deselect_node(self):
        self.ids.ideaBucketTreeView._selected_node.is_selected = False
        self.ids.ideaBucketTreeView._selected_node = None

    def clear_tag_button_clicked(self):
        self.selectedTag = None
        self.ids.tagNameInput.text = ''
        

    def clear_idea_button_clicked(self):
        self.selectedIdea = None
        self.ids.ideaNameInput.text = ''
        self.ids.ideaDescriptionInput.text = ''

    def add_tag_button_clicked(self):
        tag_name = self.ids.tagNameInput.text
        if(len(tag_name) != 0):
            ideaBucket.add_tag({'name' : tag_name})
            self.refresh_idea_tree()
    
    def delete_tag_button_clicked(self):
        ideaBucket.remove_tag(self.selectedTag)
        self.refresh_idea_tree()

    def add_idea_button_clicked(self):
        if(self.selectedTag is not None):
            idea_name = self.ids.ideaNameInput.text
            idea_description = self.ids.ideaDescriptionInput.text
            ideaBucket.add_idea({'name' : idea_name, 'description' : idea_description, 'tag' : self.selectedTag})
            self.refresh_idea_tree()\
        
    def save_tag_button_clicked(self):
        new_name = self.ids.tagNameInput.text
        ideaBucket.change_tag(self.selectedTag, new_name)
        self.refresh_idea_tree()

    def save_idea_button_clicked(self):
        idea_name = self.ids.ideaNameInput.text
        idea_description = self.ids.ideaDescriptionInput.text
        ideaBucket.change_idea(self.selectedIdea, idea_name, idea_description, self.ids.tag_spinner.text)
        self.refresh_idea_tree()

    def delete_idea_button_clicked(self):
        for idea in ideaBucket.ideas:
            if(idea['name'] == self.selectedIdea):
                ideaBucket.remove_idea(idea)
                self.refresh_idea_tree()
                self.clear_idea_button_clicked()
                break