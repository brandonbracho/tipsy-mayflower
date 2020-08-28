import gmaps 

search_results = response.json()
spots = search_results['businesses']
formatted_address = []
for spot in spots:
    name = spot['name']
    for key, value in spot['location'].items():
        if key == 'display_address':
            if len(value) == 2:
                new = value[0] + ', ' + value[1]
            else:
                new = value[0]+', ' + value[1] + ' ' + value[2]
                
            together = f'({name}), {new}'
            formatted_address.append(together)

#organize coordinates from yelp in a dictionary
pop_dict={}
for spot in spots:
    name=spot['name']
    coord=spot['coordinates']
    for key,value in coord.items():
        pop_dict[name]=(coord['latitude'],coord['longitude'])
print(pop_dict)

#code below adds coordinates to response_list dictionaries 
for values in pop_dict.values():
    for n in response_list:
        n['coordinates']=values
        
#updated_list contains coordinates of location if current_popularity is not None. 
updated_list=[n['coordinates'] for n in response_list if n['current_popularity']!=None]

#weight contains current_popularity if the value is not None
weight=[n['current_popularity'] for n in response_list if n['current_popularity']!=None]

gmaps.configure(api_key='AIzaSyCobJCcwLjJzFw2Iz_1R66wWXqotu2rJTM')
figure=gmaps.figure()
figure.add_layer(gmaps.heatmap_layer(updated_list,weights=weight,point_radius=20))

figure

