from typing import List, Dict, Optional, Union, Any, Iterator, Mapping

from .base import APIBase, Item, ItemList


GET_LIMIT = 200
POST_LIMIT = 500
PUT_LIMIT = 500

SORT_ORDER = {
    'name': 0,
    'id': 3,
    'createdAt': 2,
    'updatedAt': 1,
}


class CompanyModels(APIBase):
    ######
    # URLs
    ######


    def get_company_econ_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of company econ models.
        """
        url = f'{self.API_BASE_URL}/econ-models'
        if filters is None:
            return url

        url += self._build_params_string(filters)
        return url


    def get_company_econ_models_by_type_url(
            self, econ_model_type: str, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of econ models for a specific project id and model
        type. Allows `econModelType` passed as a parameter rather than calling
        a different function for each model type.
        """
        def _get_route_for_model(econ_model_type: str) -> Union[str, None]:
            for model in APIBase.ECON_MODELS:
                if model['econModelType'].casefold() == econ_model_type.casefold():
                    return model['route']

            return None

        route = _get_route_for_model(econ_model_type)
        assert route is not None, f'Invalid econ model type: {econ_model_type}'
        url = f'{self.API_BASE_URL}/econ-models/{route}'
        if filters is None:
            return url

        url += self._build_params_string(filters)
        return url


    def get_company_econ_model_by_type_by_id_url(
            self, econ_model_type: str, model_id: str,
            filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of a sepcific econ model for a specific project id
        and model type. Allows `econModelType` passed as a parameter rather
        than calling a different function for each model type.
        """
        base_url = self.get_company_econ_models_by_type_url(econ_model_type)
        url = f'{base_url}/{model_id}'
        if filters is None:
            return url

        url += self._build_params_string(filters)
        return url


    def get_company_general_options_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of general options models for a specific project id.
        """
        econ_model_type = 'GeneralOptions'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_general_options_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific general options model for a specific
        project id.
        """
        econ_model_type = 'GeneralOptions'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_actual_forecast_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of actual-forecast models for a specific project id.
        """
        econ_model_type = 'ActualOrForecast'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_actual_forecast_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific actual-forecast model for a specific
        project id.
        """
        econ_model_type = 'ActualOrForecast'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_capex_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of capex models for a specific project id.
        """
        econ_model_type = 'Capex'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_capex_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific capex model for a specific
        project id.
        """
        econ_model_type = 'Capex'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_date_settings_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of date settings models for a specific project id.
        """
        econ_model_type = 'Dates'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)

    def get_company_date_settings_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific date settings model for a specific
        project id.
        """
        econ_model_type = 'Dates'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_depreciation_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of depreciation models for a specific project id.
        """
        econ_model_type = 'Depreciation'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_depreciation_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific depreciation model for a specific
        project id.
        """
        econ_model_type = 'Depreciation'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_differentials_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of differentials models for a specific project id.
        """
        econ_model_type = 'Differentials'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_differentials_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific differentials model for a specific
        project id.
        """
        econ_model_type = 'Differentials'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_emissions_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of emissions models for a specific project id.
        """
        econ_model_type = 'Emission'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_emissions_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific emissions model for a specific
        project id.
        """
        econ_model_type = 'Emission'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_escalations_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of escalations models for a specific project id.
        """
        econ_model_type = 'Escalation'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_escalations_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific escalations model for a specific
        project id.
        """
        econ_model_type = 'Escalation'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_expenses_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of expenses models for a specific project id.
        """
        econ_model_type = 'Expenses'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_expenses_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific expenses model for a specific
        project id.
        """
        econ_model_type = 'Expenses'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_fluid_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of fluid models for a specific project id.
        """
        econ_model_type = 'FluidModel'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_fluid_models_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific fluid model for a specific
        project id.
        """
        econ_model_type = 'FluidModel'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_ownership_reversions_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of ownership reversions models for a specific
        project id.
        """
        econ_model_type = 'OwnershipReversion'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_ownership_reversions_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific ownership reversions model for a
        specific project id.
        """
        econ_model_type = 'OwnershipReversion'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_pricing_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of pricing models for a specific project id.
        """
        econ_model_type = 'Pricing'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_pricing_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific pricing model for a specific
        project id.
        """
        econ_model_type = 'Pricing'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_production_taxes_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of production taxes models for a specific
        project id.
        """
        econ_model_type = 'ProductionTaxes'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_production_taxes_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific production taxes model for a specific
        project id.
        """
        econ_model_type = 'ProductionTaxes'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_reserves_categories_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of reserves categories models for a specific
        project id.
        """
        econ_model_type = 'ReservesCategory'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_reserves_categories_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific reserves categories model for a
        specific project id.
        """
        econ_model_type = 'ReservesCategory'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_riskings_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of riskings models for a specific project id.
        """
        econ_model_type = 'Risking'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_riskings_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific riskings model for a specific
        project id.
        """
        econ_model_type = 'Risking'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    def get_company_stream_properties_models_url(self, filters: Optional[Dict[str, str]] = None) -> str:
        """
        Returns the API url of stream properties models for a specific
        project id.
        """
        econ_model_type = 'StreamProperties'
        return self.get_company_econ_models_by_type_url(econ_model_type, filters)


    def get_company_stream_properties_model_by_id_url(self, model_id: str) -> str:
        """
        Returns the API url of a specific stream properties model for a
        specific project id.
        """
        econ_model_type = 'StreamProperties'
        return self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)


    ###########
    # API calls
    ###########


    def get_company_econ_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of company econ models.
        """
        url = self.get_company_econ_models_url(filters)
        params = {'take': GET_LIMIT}
        econ_models = self._get_items(url, params)

        return self._keysort(econ_models, SORT_ORDER)


    def get_company_econ_models_by_type(
            self, econ_model_type: str, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of econ models by type. Allows `econModelType` passed as
        a parameter rather than calling a different function for each model
        type.
        """
        url = self.get_company_econ_models_by_type_url(econ_model_type, filters)
        params = {'take': GET_LIMIT}
        econ_models = self._get_items(url, params)

        return self._keysort(econ_models, SORT_ORDER)


    def get_company_econ_model_by_type_by_id(
            self, econ_model_type: str, model_id: str) -> Union[Item, None]:
        """
        Returns a specific econ model from its type and id. Allows
        `econModelType` passed as a parameter rather than calling a different
        function for each model type.
        """
        url = self.get_company_econ_model_by_type_by_id_url(econ_model_type, model_id)
        econ_model = self._get_items(url)

        return econ_model[0]


    def get_company_general_options_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of general options models.
        """
        url = self.get_company_general_options_models_url(filters)
        params = {'take': GET_LIMIT}
        general_options = self._get_items(url, params)

        return self._keysort(general_options, SORT_ORDER)


    def get_company_general_options_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific general options model from its id.
        """
        url = self.get_company_general_options_model_by_id_url(model_id)
        general_options = self._get_items(url)

        return general_options[0]


    def get_company_actual_forecast_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of actual-forecast models.
        """
        url = self.get_company_actual_forecast_models_url(filters)
        params = {'take': GET_LIMIT}
        actual_forecast = self._get_items(url, params)

        return self._keysort(actual_forecast, SORT_ORDER)


    def get_company_actual_forecast_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific actual-forecast model from its id.
        """
        url = self.get_company_actual_forecast_model_by_id_url(model_id)
        actual_forecast = self._get_items(url)

        return actual_forecast[0]


    def get_company_reserves_categories_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of reserves categories models.
        """
        url = self.get_company_reserves_categories_models_url(filters)
        params = {'take': GET_LIMIT}
        reserves_categories = self._get_items(url, params)

        return self._keysort(reserves_categories, SORT_ORDER)


    def get_company_reserves_categories_by_id(self, model_id: str) -> Item:
        """
        Returns a specific reserves categories model from its id.
        """
        url = self.get_company_reserves_categories_model_by_id_url(model_id)
        reserves_categories = self._get_items(url)

        return reserves_categories[0]


    def get_company_escalation_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of escalations models.
        """
        url = self.get_company_escalations_models_url(filters)
        params = {'take': GET_LIMIT}
        escalations = self._get_items(url, params)

        return self._keysort(escalations, SORT_ORDER)


    def get_company_escalations_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific escalations model from its id.
        """
        url = self.get_company_escalations_model_by_id_url(model_id)
        escalations = self._get_items(url)

        return escalations[0]


    def get_company_differential_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of differentials models.
        """
        url = self.get_company_differentials_models_url(filters)
        params = {'take': GET_LIMIT}
        differentials = self._get_items(url, params)

        return self._keysort(differentials, SORT_ORDER)


    def get_company_differentials_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific differentials model from its id.
        """
        url = self.get_company_differentials_model_by_id_url(model_id)
        differentials = self._get_items(url)

        return differentials[0]


    def get_company_pricing_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of pricing models.
        """
        url = self.get_company_pricing_models_url(filters)
        params = {'take': GET_LIMIT}
        pricing = self._get_items(url, params)

        return self._keysort(pricing, SORT_ORDER)


    def get_company_pricing_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific pricing model from its id.
        """
        url = self.get_company_pricing_model_by_id_url(model_id)
        pricing = self._get_items(url)

        return pricing[0]


    def get_company_ownership_reversions_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of ownership reversions models.
        """
        url = self.get_company_ownership_reversions_models_url(filters)
        params = {'take': GET_LIMIT}
        ownership_reversions = self._get_items(url, params)

        return self._keysort(ownership_reversions, SORT_ORDER)


    def get_company_ownership_reversions_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific ownership reversions model from its id.
        """
        url = self.get_company_ownership_reversions_model_by_id_url(model_id)
        ownership_reversions = self._get_items(url)

        return ownership_reversions[0]


    def get_company_production_taxes_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of production taxes models.
        """
        url = self.get_company_production_taxes_models_url(filters)
        params = {'take': GET_LIMIT}
        production_taxes = self._get_items(url, params)

        return self._keysort(production_taxes, SORT_ORDER)


    def get_company_production_taxes_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific production taxes model from its id.
        """
        url = self.get_company_production_taxes_model_by_id_url(model_id)
        production_taxes = self._get_items(url)

        return production_taxes[0]


    def get_company_risking_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of riskings models.
        """
        url = self.get_company_riskings_models_url(filters)
        params = {'take': GET_LIMIT}
        riskings = self._get_items(url, params)

        return self._keysort(riskings, SORT_ORDER)


    def get_company_riskings_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific riskings model from its id.
        """
        url = self.get_company_riskings_model_by_id_url(model_id)
        riskings = self._get_items(url)

        return riskings[0]


    def get_company_stream_properties_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of stream properties models.
        """
        url = self.get_company_stream_properties_models_url(filters)
        params = {'take': GET_LIMIT}
        stream_properties = self._get_items(url, params)

        return self._keysort(stream_properties, SORT_ORDER)


    def get_company_stream_properties_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific stream properties model from its id.
        """
        url = self.get_company_stream_properties_model_by_id_url(model_id)
        stream_properties = self._get_items(url)

        return stream_properties[0]


    def get_company_expense_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of expenses models.
        """
        url = self.get_company_expenses_models_url(filters)
        params = {'take': GET_LIMIT}
        expenses = self._get_items(url, params)

        return self._keysort(expenses, SORT_ORDER)


    def get_company_expenses_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific expenses model from its id.
        """
        url = self.get_company_expenses_model_by_id_url(model_id)
        expenses = self._get_items(url)

        return expenses[0]


    def get_company_emission_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of emissions models.
        """
        url = self.get_company_emissions_models_url(filters)
        params = {'take': GET_LIMIT}
        emissions = self._get_items(url, params)


        return self._keysort(emissions, SORT_ORDER)


    def get_company_emissions_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific emissions model from its id.
        """
        url = self.get_company_emissions_model_by_id_url(model_id)
        emissions = self._get_items(url)

        return emissions[0]


    def get_company_fluid_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of fluid models.
        """
        url = self.get_company_fluid_models_url(filters)
        params = {'take': GET_LIMIT}
        fluid_models = self._get_items(url, params)

        return self._keysort(fluid_models, SORT_ORDER)


    def get_company_fluid_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific fluid model from its id.
        """
        url = self.get_company_fluid_models_by_id_url(model_id)
        fluid_models = self._get_items(url)

        return fluid_models[0]


    def get_company_capex_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of capex models.
        """
        url = self.get_company_capex_models_url(filters)
        params = {'take': GET_LIMIT}
        capex = self._get_items(url, params)

        return self._keysort(capex, SORT_ORDER)


    def get_company_capex_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific capex model from its id.
        """
        url = self.get_company_capex_model_by_id_url(model_id)
        capex = self._get_items(url)

        return capex[0]


    def get_company_date_settings_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of date settings models.
        """
        url = self.get_company_date_settings_models_url(filters)
        params = {'take': GET_LIMIT}
        date_settings = self._get_items(url, params)

        return self._keysort(date_settings, SORT_ORDER)


    def get_company_date_settings_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific date settings model from its id.
        """
        url = self.get_company_date_settings_model_by_id_url(model_id)
        date_settings = self._get_items(url)

        return date_settings[0]


    def get_company_depreciation_models(self, filters: Optional[Dict[str, str]] = None) -> ItemList:
        """
        Returns a list of depreciation models.
        """
        url = self.get_company_depreciation_models_url(filters)
        params = {'take': GET_LIMIT}
        depreciation = self._get_items(url, params)

        return self._keysort(depreciation, SORT_ORDER)


    def get_company_depreciation_model_by_id(self, model_id: str) -> Item:
        """
        Returns a specific depreciation model from its id.
        """
        url = self.get_company_depreciation_model_by_id_url(model_id)
        depreciation = self._get_items(url)

        return depreciation[0]