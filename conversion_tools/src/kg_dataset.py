# -*- coding: utf-8 -*-
# @Time   : 2020/10/29
# @Author : Shanlei Mu
# @Email  : slmu@ruc.edu.cn

import os


class KGDataset(object):
    def __init__(self, dataset, inter_file, kg_data_path, output_path, hop):
        super(KGDataset, self).__init__()

        # load
        self.extra_kg_file = os.path.join(kg_data_path, 'extra.kg')
        self.kg_file_list = [os.path.join(kg_data_path,
                                          'hop' + str(i + 1) + '.kg') for i in range(3)]
        self.output_link_file = os.path.join(output_path, dataset + '.link')
        self.output_kg_file = os.path.join(output_path, dataset + '.kg')

        self.hop = hop

        self.seed_entities, self.seed_link, self.item_field = \
            self.get_seed_entities(inter_file, os.path.join(kg_data_path, 'link.kg'))
        self.selected_relations = self.get_selected_relations(os.path.join(kg_data_path, 'relation.kg'))

    @staticmethod
    def get_seed_entities(inter_file, link_file):
        items = set()
        with open(inter_file, 'r') as fp:
            item_field = fp.readline().strip().split('\t')[1].strip().split(':')[0]
            for line in fp:
                item = line.strip().split('\t')[1]
                items.add(item)

        item2entity_dict = dict()
        with open(link_file, 'r') as fp:
            for line in fp:
                item, entity = line.strip().split('\t')
                item2entity_dict[item] = entity

        seed_entities = set()
        seed_link = dict()
        for item in items:
            if item in item2entity_dict:
                seed_entities.add(item2entity_dict[item])
                seed_link[item] = item2entity_dict[item]
        return seed_entities, seed_link, item_field

    @staticmethod
    def get_selected_relations(relation_file):
        relations = set()
        with open(relation_file, 'r') as fp:
            for line in fp:
                relations.add(line.strip())
        return relations

    def generate_link(self):
        with open(self.output_link_file, 'w') as fp:
            fp.write(self.item_field + ':token\tentity_id:token\n')
            for item in self.seed_link:
                fp.write(str(item) + '\t' + self.seed_link[item] + '\n')

    def generate_knowledge(self):

        def extract_hop_graph(graph_file, relations, seeds, histories):
            triples = []
            entities = set()
            with open(graph_file, 'r') as fp:
                for line in fp:
                    h, r, t = line.strip().split('\t')
                    if r in relations and (h in seeds or t in seeds):
                        triples.append(line)
                        entities.add(h)
                        entities.add(t)
            return entities - histories, triples

        def extract_extra_graph(graph_file, relations, histories):
            triples = []
            with open(graph_file, 'r') as fp:
                for line in fp:
                    h, r, t = line.strip().split('\t')
                    if r in relations and (h in histories or t in histories):
                        triples.append(line)
            return triples

        history_entities = set()
        hop_triples = []
        seed_entities = self.seed_entities
        extra_kg_file = self.extra_kg_file
        for i in range(self.hop):
            kg_file = self.kg_file_list[i]
            history_entities |= seed_entities

            seed_entities, temp_triples = extract_hop_graph(kg_file, self.selected_relations,
                                                            seed_entities, history_entities)
            hop_triples += temp_triples
        extra_triples = extract_extra_graph(extra_kg_file, self.selected_relations,
                                            history_entities)

        final_triples = hop_triples + extra_triples

        with open(self.output_kg_file, 'w') as fp:
            fp.write('head_id:token\trelation_id:token\ttail_id:token\n')
            for triple in final_triples:
                fp.write(triple)
