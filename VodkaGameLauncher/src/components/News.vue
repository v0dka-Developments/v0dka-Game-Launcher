 
    <div class="col-fixed" style="width:500px; height:500px;">
        <div class="card" v-if="show_more && total_news">
          <Carousel
            :value="news_feed"
            :numVisible="1"
            :numScroll="1"
            circular
            :autoplayInterval="3000"
          >
            <template #item="slotProps">
              <div class="border-1 surface-border border-round m-2 text-center py-5 px-3">
                <div class="mb-3">
                  <Avatar
                    v-if="slotProps.data.image && slotProps.data.image.length > 1"
                    :image="'https://primefaces.org/cdn/primevue/images/product/' + slotProps.data.image"
                    class="mr-2"
                    size="xlarge"
                  />
                  <Avatar
                    v-if="!slotProps.data.image"
                    :alt="slotProps.data.name"
                    class="mr-2 default_image"
                    size="xlarge"
                  />
                </div>
                <div>
                  <Tag
                    :value="slotProps.data.typeofupdate"
                    :severity="getSeverity(slotProps.data.typeofupdate)"
                  />
                  <h4 class="mb-1">{{ slotProps.data.name }}</h4>
                  <h6 class="mt-0 mb-3">{{ slotProps.data.description.substr(0, 30) + " ..." }}</h6>
                  <Button label="Read More" severity="success" />
                </div>
              </div>
            </template>
          </Carousel>
        </div>
  
        <div class="card" v-if="!show_more ">
          
          <Carousel :value="news_feed" :numVisible="1" :numScroll="1">
            <template #item="slotProps">
              <div class="border-1 surface-border border-round m-2 text-center py-5 px-3">
                <div class="mb-3">
                  <Avatar
                    v-if="slotProps.data.image && slotProps.data.image.length > 1"
                    :image="'https://primefaces.org/cdn/primevue/images/product/' + slotProps.data.image"
                    class="mr-2"
                    size="xlarge"
                  />
                  <Avatar
                    v-if="!slotProps.data.image"
                    :alt="slotProps.data.name"
                    class="mr-2 default_image"
                    size="xlarge"
                  />
                </div>
                <div>
                  <Tag
                    :value="slotProps.data.typeofupdate"
                    :severity="getSeverity(slotProps.data.typeofupdate)"
                  />
                  <h4 class="mb-1">{{ slotProps.data.name }}</h4>
                  <h6 class="mt-0 mb-3">{{ slotProps.data.description.substr(0, 30) + " ..." }}</h6>
                  <Button label="Read More" severity="success" />
                </div>
              </div>
            </template>
          </Carousel>
        </div>
  
        <div class="card" v-if="!total_news">
  
          <Carousel :value="default_data" :numVisible="1" :numScroll="1">
            <template #item="slotProps">
              <div class="border-1 surface-border border-round m-2 text-center py-5 px-3">
                <div class="mb-3">
                  <Avatar
                    v-if="!slotProps.data.image"
                    :alt="slotProps.data.name"
                    class="mr-2 default_image"
                    size="xlarge"
                  />
                </div>
                <div>
                  <Tag
                    :value="slotProps.data.typeofupdate"
                    :severity="getSeverity(slotProps.data.typeofupdate)"
                  />
                  <h4 class="mb-1">{{ slotProps.data.name }}</h4>
                  <h6 class="mt-0 mb-3">{{ slotProps.data.description.substr(0, 30) + " ..." }}</h6>
                  
                </div>
              </div>
            </template>
          </Carousel>
          
        </div>
      </div>