from scipy import spatial
import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(APP_ROOT, 'recommend_data/')


class Recommendation(object):

    def get_feature_vector(self, small_list, full_list):
        vec_len = len(full_list)
        returned_list = [0] * vec_len
        for item in small_list:
            if item in full_list:
                index = full_list.index(item)
                returned_list[index] = 1
        return returned_list

    def get_company_data(self, csv_file):
        out1 = open(csv_file, "rb")
        out_dict = {}
        for line in out1:
            tokens = line.split("\t")
            company_name = tokens[0]
            company_class = tokens[1]
            company_vector = tokens[2:-1]
            out_dict[company_name] = (company_class, company_vector)
        return out_dict

    def get_score(self, feature_vector, company_vector):
        # print sum(feature_vector)
        # print sum(company_vector)
        return 1 - spatial.distance.cosine(feature_vector, company_vector)

    def get_recommendations(self, data_folder, small_list):
        try:
            full_list = open(data_folder + "full_list.txt", "rb").read().split("\n")
            # print ", ".join(full_list)
            csv_file = data_folder + "csv_input.txt"
            v1 = self.get_feature_vector(small_list, full_list)
            company_data = self.get_company_data(csv_file)
            category_dict = {}
            max_score = 0
            max_category = 0
            # v1 = get_feature_vector(feature_vector, full_list)
            # print sum(v1)
            # sys.exit(0)
            # print ", ".join(map(str, v1))

            for item in company_data:
                company_name = item
                company_vector = company_data[item][1]
                company_category = company_data[item][0]
                if company_category in category_dict:
                    category_list = category_dict[company_category]
                else:
                    category_list = []
                v2 = self.get_feature_vector(company_vector, full_list)
                score = self.get_score(v1, v2)
                #print score
                company_tuple = (company_name, score)
                category_list.append(company_tuple)
                category_dict[company_category] = category_list
                if score > max_score:
                    max_score = score
                    max_category = company_category
            # print max_category
            # print max_score

            category_list = category_dict[max_category]
            category_list = sorted(category_list, key=lambda x: x[1], reverse=True)
            returned_company_list = []
            for items in category_list:
                returned_company_list.append(items[0].strip('.html'))
            return returned_company_list

        except KeyError:
            return []


list1 = ["Crowdsourcing", "B2B", "Atlanta", "Training"]
list2 = ["Cambridge", "Digital Media", "Education", "Analytics", "Politics"]
list3 = ["University Students", "Mobile", "Recruting", "Educational Games", "Big Data"]
print DATA_FOLDER
print Recommendation().get_recommendations(DATA_FOLDER, list1)
print Recommendation().get_recommendations(DATA_FOLDER, list2)
print Recommendation().get_recommendations(DATA_FOLDER, list3)

